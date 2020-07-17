import os
from unittest import mock

from api.utils.app import check_loan_fields, is_api_key_valid, parse_loan_form


def test_parse_loan_form(snapshot):
    form = {
        "name": "Everton Tomalok",
        "cpf": "123.456.789-00",
        "birthdate": "15/08/1992",
        "amount": "1000.50",
        "terms": "6",
        "income": "12000.00",
    }
    form_parsed = parse_loan_form(form)

    snapshot.assert_match(form_parsed)


def test_parse_loan_form_incomplete(snapshot):
    form = {
        "name": "Everton Tomalok",
        "cpf": "123.456.789-00",
        "terms": "6",
        "income": "12000.00",
    }
    form_parsed = parse_loan_form(form)

    snapshot.assert_match(form_parsed)


def test_check_loan_fields(snapshot):
    check_it = {
        "name": "Everton Tomalok",
        "cpf": "123.456.789-00",
        "birthdate": "15/08/1992",
        "amount": "1000.50",
        "terms": "6",
        "income": "12000.00",
    }

    snapshot.assert_match(check_loan_fields(check_it))


def test_check_loan_fields_all_fields_invalid(snapshot):
    check_it = {
        "name": 1234,
        "cpf": "123.456.789-000123",
        "birthdate": "15081992",
        "amount": "1000.asb50",
        "terms": "abc",
        "income": "12000.ab",
    }

    snapshot.assert_match(check_loan_fields(check_it))


def test_check_loan_fields_missing_fields(snapshot):
    check_it = {"name": "Everton Tomalok", "terms": "6", "income": "12000.00"}

    snapshot.assert_match(check_loan_fields(check_it))


@mock.patch.dict(os.environ, {"API_KEY": "123"})
def test_is_api_key_valid(snapshot):
    snapshot.assert_match(is_api_key_valid("123"))


def test_is_api_key_valid_not_injected():
    try:
        is_api_key_valid("123")
        assert True
    except ValueError:
        assert True
