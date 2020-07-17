import mongomock

from api.model import Client, Loan
from api.model.database import Database
from api.model.utils import parse_model_and_validate
from api.utils.dates import parse_str_to_date


def test_insert_client(snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = "uuid-1234"
    data = {
        "_id": _id,
        "name": "Everton Tomalok",
        "cpf": "12345678900",
        "birthdate": parse_str_to_date("15/08/1992"),
        "amount": 3000,
        "terms": 6,
        "income": 12000,
    }

    client = parse_model_and_validate(data, Client)
    db._insert_client(client.data)
    client_inserted = db.find_client(_id)

    snapshot.assert_match(client_inserted)


def test_with_database():
    try:
        with Database():
            opened = True
        assert opened
    except Exception:
        print("The MongoDB wasn't found in your machine!")


def test_insert_loan(loan_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    loan = parse_model_and_validate(loan_fixture, Loan)
    snapshot.assert_match(loan.status)
    snapshot.assert_match(loan.data)

    db._insert_loan(loan.data)
    loan_inserted = db.find_loan(loan_fixture["_id"])

    snapshot.assert_match(loan_inserted)


def test_start_process(snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = "uuid_1234"
    data = {
        "_id": _id,
        "name": "Everton Tomalok",
        "cpf": "12345678900",
        "birthdate": parse_str_to_date("15/08/1992"),
        "amount": 3000,
        "terms": 6,
        "income": 12000,
    }

    insert_status = db.start_process(data)
    assert insert_status.status

    client_inserted = db.find_client(_id)
    loan_inserted = db.find_loan(_id)

    snapshot.assert_match(client_inserted)
    snapshot.assert_match(loan_inserted)


def test_start_process_error():
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = "uuid_1234"
    data = {
        "_id": _id,
        "birthdate": parse_str_to_date("15/08/1992"),
        "amount": 3000,
        "terms": 6,
        "income": 12000,
    }

    insert_status = db.start_process(data)
    assert not insert_status.status


def test_set_loan_refused_by_age(loan_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = loan_fixture["_id"]

    db.loan_collection.insert_one(loan_fixture)
    db.find_and_set_loan_refused_by_age(_id)

    snapshot.assert_match(db.find_loan(_id))


def test_set_loan_refused_by_score(loan_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = loan_fixture["_id"]
    score = 300

    db.loan_collection.insert_one(loan_fixture)
    db.find_and_set_loan_refused_by_score(_id, score)

    snapshot.assert_match(db.find_loan(_id))


def test_set_loan_accept(loan_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = loan_fixture["_id"]
    info = {"_id": _id, "score": 954, "amount": 4000.00, "terms": 9, "commitment": 0.3}

    db.loan_collection.insert_one(loan_fixture)
    db.find_and_set_loan_accept(**info)

    snapshot.assert_match(db.find_loan(_id))


def test_set_loan_refused_by_pmt(loan_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = loan_fixture["_id"]
    info = {"_id": _id, "score": 954, "commitment": 0.3}

    db.loan_collection.insert_one(loan_fixture)
    db.find_and_set_loan_refused_by_commitment(**info)

    snapshot.assert_match(db.find_loan(_id))


def test_set_loan_task_error(loan_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    _id = loan_fixture["_id"]

    try:
        raise ValueError("Raising an error")
    except Exception as err:
        info = {"_id": _id, "err": err}

        db.loan_collection.insert_one(loan_fixture)
        db.set_loan_task_error(**info)

        loan = db.find_loan(_id)
        assert "last_err" in loan["metadata"]["err"]

        del loan["metadata"]["err"]["last_err"]

        snapshot.assert_match(loan)


def test_delete_loan_and_cliente(loan_fixture, client_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    loan_id = loan_fixture["_id"]
    client_id = client_fixture["_id"]

    assert loan_id == client_id

    db._insert_client(client_fixture)
    db._insert_loan(loan_fixture)

    loan = db.find_loan(loan_id)
    client = db.find_client(client_id)

    snapshot.assert_match(loan)
    snapshot.assert_match(client)

    db.delete_loan_and_client(client_id)

    loan = db.find_loan(loan_id)
    client = db.find_client(client_id)

    snapshot.assert_match(loan)
    snapshot.assert_match(client)
