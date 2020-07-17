import logging

from api.celeryqueue.celery import celery
from api.model.database import Database
from api.policy import AgePolicy, ScorePolicy, CommitmentPolicy


logger = logging.getLogger()


@celery.task(name="loan.process")
def find(_id):
    cpf, income, amount, birth_date = get_client_info(_id)
    if not cpf:
        return False

    try:
        age_policy_status, age_metadata = AgePolicy(_id, birth_date).check()
        if not age_policy_status.status:
            return age_policy_status.loan

        score_policy_status, score_metadata = ScorePolicy(_id, cpf).check()
        if not score_policy_status.status:
            return score_policy_status.loan

        commitment_policy_status, commitment_metadata = CommitmentPolicy(
            _id,
            amount,
            income,
            cpf,
            score_metadata.get("metadata", {}).get("score")
        ).check()

        return commitment_policy_status.loan

    except Exception as err:
        logger.error(
            f"An error occurred when processing id {id}\n"
            f"type err: {type(err)}\n"
            f"Description: {err}"
        )

        # Set error metadata in Database
        with Database() as db:
            db.set_loan_task_error(_id, err)

        # Rerun it in 5 minutes
        find.apply_async(args=[_id], countdown=300)


def get_client_info(_id):
    with Database() as db:
        client = db.find_client(_id)
        return (
            client["cpf"],
            float(client["income"]),
            float(client["amount"]),
            client["birthdate"],
        )
