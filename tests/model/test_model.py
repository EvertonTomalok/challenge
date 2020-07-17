from datetime import date

from api.model import Client, Loan
from api.model.utils import parse_model_and_validate


def _handle_client_err(client_err):
    client_err.data["data_received"]["birthdate"] = str(
        client_err.data["data_received"]["birthdate"]
    )

    return client_err


def test_parse_and_validate(snapshot):
    data = {
        "name": "Everton Tomalok",
        "cpf": "12345678900",
        "birthdate": date(1992, 8, 15),
        "amount": 4000,
        "terms": 6,
        "income": 12000,
    }

    client_validated = parse_model_and_validate(data, Client)
    del client_validated.data["_id"]

    client_ok = client_validated.status
    client_data = client_validated.data

    assert client_ok == 1
    snapshot.assert_match(client_data)


def test_client(snapshot):
    client = Client(
        {
            "name": "Everton Tomalok",
            "cpf": "12345678900",
            "birthdate": date(1992, 8, 15),
            "amount": 4000,
            "terms": 6,
            "income": 12000,
        }
    )
    client.validate()

    client_parsed = client.to_primitive()
    del client_parsed["_id"]

    snapshot.assert_match(client_parsed)


def test_client_data_error(snapshot):
    data = {
        "name": "Everton Tomalok",
        "birthdate": date(1992, 8, 15),
        "terms": 6,
        "income": 12000,
    }

    client_err = parse_model_and_validate(data, Client)
    client_err = _handle_client_err(client_err)

    client_not_ok = client_err.status
    client_data = client_err.data

    assert client_not_ok == 0
    snapshot.assert_match(client_data)


def test_client_data_min_max_value_error(snapshot):
    data = {
        "name": "Everton Tomalok",
        "cpf": "12345678900",
        "birthdate": date(1992, 8, 15),
        "amount": 6000,
        "terms": 3,
        "income": 12000,
    }

    client_err = parse_model_and_validate(data, Client)
    client_err = _handle_client_err(client_err)

    client_not_ok = client_err.status
    client_data = client_err.data

    assert client_not_ok == 0
    snapshot.assert_match(client_data)


def test_loan_initialize(snapshot):
    data = {"_id": "uuid-1234"}

    loan = parse_model_and_validate(data, Loan)

    loan_status_ok = loan.status
    loan_data = loan.data

    assert loan_status_ok == 1
    snapshot.assert_match(loan_data)


def test_loan_no_uuid(snapshot):
    data = {"terms": 6}

    loan = parse_model_and_validate(data, Loan)

    loan_status_not_ok = loan.status
    loan_data = loan.data

    assert loan_status_not_ok == 0
    snapshot.assert_match(loan_data)


def test_loan_error_amount_and_terms(snapshot):
    data = {"_id": "uuid-5678", "terms": 15, "amount": 10000}

    loan = parse_model_and_validate(data, Loan)

    loan_status_not_ok = loan.status
    loan_data = loan.data

    assert loan_status_not_ok == 0
    snapshot.assert_match(loan_data)
