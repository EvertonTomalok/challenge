from collections import namedtuple
from datetime import datetime, timedelta

import mongomock
from pymongo import MongoClient

from api.model import Client, Loan
from api.model.config import MONGODB_SETTINGS
from api.model.utils import parse_model_and_validate
from api.utils.enumerators import ProcessingStatus, RefusePolicy, ResultStatus, Status

ProcessStatus = namedtuple("ProcessStatus", "status id data")


class Database:
    __client = None
    __database = None

    def __init__(self, db_test=None):
        self.__setup(db_test)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__teardown()

    def __del__(self):
        self.__teardown()

    def __setup(self, db_test):
        if not self.__client:
            if not db_test:
                self.__client = MongoClient(MONGODB_SETTINGS["url"])
            else:
                self.__client = (
                    mongomock.MongoClient()["Test"]
                    if isinstance(db_test, str)
                    else db_test
                )

            self.__database = self.__client["challenge"]
            self.loan_collection = self.__database.loan
            self.clients_collection = self.__database.clients

    def __teardown(self):
        if self.__client:
            try:
                self.__client.close()
            except TypeError:
                pass

    def _insert_client(self, data):
        self.clients_collection.insert_one(data)

    def _insert_loan(self, data):
        self.loan_collection.insert_one(data)

    def start_process(self, data) -> ProcessStatus:

        client = parse_model_and_validate(data, Client)

        if client.status:
            _id = client.data["_id"]
            loan = parse_model_and_validate({"_id": _id}, Loan)

            self._insert_client(client.data)
            self._insert_loan(loan.data)

            return ProcessStatus(Status.success.value, _id, client.data)
        return ProcessStatus(Status.error.value, None, client.data)

    def find_loan(self, _id) -> dict:
        return self.loan_collection.find_one({"_id": _id})

    def find_client(self, _id) -> dict:
        return self.clients_collection.find_one({"_id": _id})

    def find_and_set_loan_refused_by_age(self, _id) -> dict:
        self.loan_collection.update_one(
            {"_id": _id},
            {
                "$set": {
                    "status": ProcessingStatus.completed.value,
                    "result": ResultStatus.refused.value,
                    "refused_policy": RefusePolicy.age.value,
                }
            },
        )
        return self.find_loan(_id)

    def find_and_set_loan_refused_by_score(self, _id, score):
        self.loan_collection.update_one(
            {"_id": _id},
            {
                "$set": {
                    "status": ProcessingStatus.completed.value,
                    "result": ResultStatus.refused.value,
                    "refused_policy": RefusePolicy.score.value,
                    "metadata": {"score": score},
                }
            },
        )
        return self.find_loan(_id)

    def find_and_set_loan_accept(self, _id, amount, terms, score, commitment):
        self.loan_collection.update_one(
            {"_id": _id},
            {
                "$set": {
                    "status": ProcessingStatus.completed.value,
                    "result": ResultStatus.approved.value,
                    "amount": amount,
                    "terms": terms,
                    "metadata": {"score": score, "commitment": commitment},
                }
            },
        )
        return self.find_loan(_id)

    def find_and_set_loan_refused_by_commitment(self, _id, score, commitment):
        self.loan_collection.update_one(
            {"_id": _id},
            {
                "$set": {
                    "status": ProcessingStatus.completed.value,
                    "result": ResultStatus.refused.value,
                    "refused_policy": RefusePolicy.commitment.value,
                    "metadata": {"score": score, "commitment": commitment},
                }
            },
        )
        return self.find_loan(_id)

    def set_loan_task_error(self, _id, err):
        self.loan_collection.update_one(
            {"_id": _id},
            {
                "$set": {
                    "metadata": {
                        "err": {
                            "last_err": str(datetime.utcnow() - timedelta(hours=3)),
                            "type": str(type(err)),
                            "description": str(err),
                        }
                    }
                }
            },
        )

    def delete_loan_and_client(self, _id):
        self.loan_collection.delete_one({"_id": _id})
        self.clients_collection.delete_one({"_id": _id})
