import pytest


@pytest.fixture(scope="module")
def loan_fixture():
    return {
        "_id": "a3289e62-c171-11ea-81ba-0242c0a88005",
        "status": "processing",
        "result": None,
        "refused_policy": None,
        "amount": None,
        "terms": None,
    }


@pytest.fixture(scope="module")
def client_fixture():
    return {
        "_id": "a3289e62-c171-11ea-81ba-0242c0a88005",
        "name": "João",
        "cpf": "12345678901",
        "birthdate": "1992-08-15",
        "amount": 1900.00,
        "income": 900.00,
        "terms": 6,
    }
