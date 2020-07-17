import json
from unittest import mock

from api.app import app


def test_get(snapshot):
    response = app.test_client().get("/")

    snapshot.assert_match(response.status_code)
    snapshot.assert_match(response.data)


def test_health(snapshot):
    response = app.test_client().get("/health")

    snapshot.assert_match(response.status_code)
    snapshot.assert_match(response.data)


def test_loan_no_api_key_provided(snapshot):
    response = app.test_client().post("/loan", data={"name": "Everton Tomalok"})
    data_resp = response.data.decode("utf-8")
    status_code = response.status_code

    snapshot.assert_match(status_code)
    snapshot.assert_match(data_resp)


@mock.patch("api.app.is_api_key_valid")
def test_loan_error_first_check(is_api_key_valid, snapshot):
    is_api_key_valid.return_value = True
    response = app.test_client().post(
        "/loan",
        data={"name": "Everton Tomalok"},
        headers={"api-key": "its a valid key"},
    )
    data_resp = json.loads(response.data.decode("utf-8"))
    snapshot.assert_match(response.status_code)
    snapshot.assert_match(data_resp)


@mock.patch("api.app.is_api_key_valid")
def test_loan_saving(is_api_key_valid, snapshot):
    is_api_key_valid.return_value = True
    json_obj = {
        "name": "Everton Tomalok",
        "cpf": "123.456.789-00",
        "birthdate": "15/08/1992",
        "amount": "1000.50",
        "terms": "6",
        "income": "12000.00",
    }
    response = app.test_client().post(
        "/loan?testingCase=true", data=json_obj, headers={"api-key": "its a valid key"}
    )
    data_resp = json.loads(response.data.decode("utf-8"))

    snapshot.assert_match(response.status_code)
    snapshot.assert_match("id" in data_resp.keys())


@mock.patch("api.app.is_api_key_valid")
def test_loan_saving_error_model(is_api_key_valid, snapshot):
    is_api_key_valid.return_value = True
    json_obj = {
        "name": "Everton Tomalok",
        "cpf": "123.456.789-00",
        "birthdate": "15/08/1992",
        "amount": "1000.50",
        "terms": "7",
        "income": "12000.00",
    }
    response = app.test_client().post(
        "/loan?testingCase=true", data=json_obj, headers={"api-key": "its a valid key"}
    )
    data_resp = json.loads(response.data.decode("utf-8"))

    snapshot.assert_match(response.status_code)
    snapshot.assert_match(data_resp)


@mock.patch("api.model.database.Database.find_loan")
def test_loan_status(find_loan):
    loan_status_value = {
        "_id": "c5b91560-1c63-43c4-91ec-925ba8a3fb87",
        "name": "Everton Tomalok",
        "cpf": "12345678900",
        "birthdate": "1992-08-15",
        "amount": "4000",
        "terms": 6,
        "income": "10000",
    }
    find_loan.return_value = loan_status_value
    response = app.test_client().get(
        "/loan/c5b91560-1c63-43c4-91ec-925ba8a3fb87?testingCase=true"
    )
    data_resp = json.loads(response.data.decode("utf-8"))

    assert data_resp == loan_status_value
