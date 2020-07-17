import threading
from os import getenv
from time import sleep

import requests

from api.model.database import Database
from tests.e2e.utils import print_message

LOAN_URL = getenv("LOAN_URL")
HEADERS = {"api-key": getenv("API_KEY_TESTING")}


@print_message
def error_request():
    payload = {"name": "João"}
    response = requests.request("POST", LOAN_URL, headers=HEADERS, data=payload)

    expected_json = {
        "errors": [
            {"cpf": "Field is Required."},
            {"birthdate": "Field is Required."},
            {"amount": "Field is Required."},
            {"income": "Field is Required."},
            {"terms": "Field is Required."},
        ]
    }

    expected = response.json() == expected_json and response.status_code == 400
    return expected


@print_message
def error_avoid_api_key():
    payload = {"name": "João"}
    response = requests.request("POST", LOAN_URL, data=payload)

    expected = response.status_code == 401
    return expected


@print_message
def error_request_model_error():
    payload = {
        "name": "João",
        "cpf": "12345678900",
        "birthdate": "1992-08-15",
        "amount": 7900.00,
        "income": 900.00,
        "terms": 7,
    }

    response = requests.request("POST", LOAN_URL, headers=HEADERS, data=payload)

    expected_json = {
        "errors": [
            {"amount": "The amount must to be between 1000.00 - 4000.00"},
            {"terms": "The terms not in [6, 9, 12]"},
        ]
    }

    expected = response.json() == expected_json and response.status_code == 400
    return expected


@print_message
def success_request_and_loan_approved():
    payload = {
        "name": "João",
        "cpf": "12345678901",
        "birthdate": "2000-03-13",
        "amount": 2900.00,
        "income": 900.00,
        "terms": 6,
    }
    response = requests.request("POST", LOAN_URL, headers=HEADERS, data=payload)
    _id = response.json()["id"]
    return looping_id_verification(_id, lambda x: x["result"] == "approved")


@print_message
def success_request_and_loan_refused_by_score():
    payload = {
        "name": "João",
        "cpf": "12345678900",
        "birthdate": "2000-03-13",
        "amount": 4000.00,
        "income": 900.00,
        "terms": 6,
    }

    response = requests.request("POST", LOAN_URL, headers=HEADERS, data=payload)
    _id = response.json()["id"]

    return looping_id_verification(
        _id, lambda x: x["result"] == "refused" and x["refused_policy"] == "score"
    )


@print_message
def success_request_and_loan_refused_by_commitment():
    payload = {
        "name": "João",
        "cpf": "12345678901",
        "birthdate": "1992-08-15",
        "amount": 4000.00,
        "income": 300.00,
        "terms": 6,
    }

    response = requests.request("POST", LOAN_URL, headers=HEADERS, data=payload)
    _id = response.json()["id"]
    return looping_id_verification(
        _id, lambda x: x["result"] == "refused" and x["refused_policy"] == "commitment"
    )


@print_message
def success_request_and_loan_refused_by_age():
    payload = {
        "name": "João",
        "cpf": "12345678901",
        "birthdate": "2012-08-15",
        "amount": 4000.00,
        "income": 300.00,
        "terms": 6,
    }

    response = requests.request("POST", LOAN_URL, headers=HEADERS, data=payload)
    _id = response.json()["id"]
    return looping_id_verification(
        _id, lambda x: x["result"] == "refused" and x["refused_policy"] == "age"
    )


def looping_id_verification(_id, function_success):
    with Database() as db:
        success = False
        i = 0
        tries = 25
        while i <= tries:
            i += 1
            client = db.loan_collection.find_one({"_id": _id})
            if client and function_success(client):
                success = True
                break
            sleep(0.3)

        db.delete_loan_and_client(_id)
    return success


if __name__ == "__main__":
    functions = [
        error_request,
        error_avoid_api_key,
        error_request_model_error,
        success_request_and_loan_approved,
        success_request_and_loan_refused_by_age,
        success_request_and_loan_refused_by_score,
        success_request_and_loan_refused_by_commitment,
    ]

    for function in functions:
        t = threading.Thread(target=function)
        t.start()
