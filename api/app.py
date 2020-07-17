import logging

from flask import Flask, abort, jsonify, request

from api.celeryqueue.celery import celery
from api.model.database import Database
from api.model.utils import prepare_data
from api.utils.app import check_loan_fields, is_api_key_valid, parse_loan_form

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def root():
    return "<h1>Challenge!</h1>"


@app.route("/health")
def health():
    return "I'm fine!"


@app.route("/loan", methods=["POST"])
def loan():
    """
    Because of the sensitive from the data and it's being included
    in the database, we'll check the data twice.

    The first time we want to detect Rogue Fields, missing Fields
    and fields with value type not allowed.

    The second verification is done by the model from the database.
    See more about this verification in the model modules.
    """

    api_key = request.headers.get("api-key")

    if not api_key or not is_api_key_valid(api_key):
        abort(401, "Forbidden access")

    data = parse_loan_form(request.form)
    # First Validation
    field_errors = check_loan_fields(data)
    if field_errors:
        error_response = {"errors": field_errors}
        return jsonify(error_response), 400

    testing = request.args.get("testingCase")
    with Database(testing) as db:
        # Second Validation
        process_status = db.start_process(prepare_data(data))

    if not process_status.status:
        error_response = {"errors": process_status.data["fields_with_error"]}

        return jsonify(error_response), 400

    # Sending id to background task
    if not testing:
        celery.send_task("loan.process", args=[process_status.id])

    return jsonify({"id": process_status.id})


@app.route("/loan/<_id>")
def get_loan_status(_id):
    testing = request.args.get("testingCase")
    with Database(testing) as db:
        loan_status = db.find_loan(_id)

    return jsonify(loan_status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
