import mongomock
import responses

from api.policy import AgePolicy, CommitmentPolicy, Database, ScorePolicy


def test_age_policy_approve(client_fixture, snapshot):
    client_fixture["birthdate"] = "1990-08-15"
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    db.start_process(client_fixture)

    age_policy_status, metadata = AgePolicy(
        client_fixture["_id"], client_fixture["birthdate"], testing=test_db
    ).check()
    snapshot.assert_match(age_policy_status.status)
    snapshot.assert_match(age_policy_status.loan)


def test_age_policy_deny(client_fixture, snapshot):
    client_fixture["birthdate"] = "2012-08-15"
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    db.start_process(client_fixture)

    age_policy_status, metadata = AgePolicy(
        client_fixture["_id"], client_fixture["birthdate"], testing=test_db
    ).check()
    snapshot.assert_match(age_policy_status.status)
    snapshot.assert_match(age_policy_status.loan)


@responses.activate
def test_score_policy_approve(client_fixture, snapshot):
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    db.start_process(client_fixture)

    score_policy_status, metadata = ScorePolicy(
        client_fixture["_id"], client_fixture["cpf"], testing=test_db
    ).check()
    snapshot.assert_match(score_policy_status.status)
    snapshot.assert_match(score_policy_status.loan)


@responses.activate
def test_score_policy_deny(client_fixture, snapshot):
    client_fixture["cpf"] = "12345678900"

    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    db.start_process(client_fixture)

    score_policy_status, metadata = ScorePolicy(
        client_fixture["_id"], client_fixture["cpf"], testing=test_db
    ).check()
    snapshot.assert_match(score_policy_status.status)
    snapshot.assert_match(score_policy_status.loan)


@responses.activate
def test_commitment_approve(client_fixture, snapshot):

    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    db.start_process(client_fixture)
    score = 900

    score_policy_status, metadata = CommitmentPolicy(
        client_fixture["_id"], 1000, 1500, client_fixture["cpf"], score, testing=test_db
    ).check()
    snapshot.assert_match(score_policy_status.status)
    snapshot.assert_match(score_policy_status.loan)


@responses.activate
def test_commitment_deny(client_fixture, snapshot):
    client_fixture["cpf"] = "12345678900"
    test_db = mongomock.MongoClient()["Test"]
    db = Database(test_db)
    db.start_process(client_fixture)

    score = 600

    score_policy_status, metadata = CommitmentPolicy(
        client_fixture["_id"], 4000, 300, client_fixture["cpf"], score, testing=test_db
    ).check()
    snapshot.assert_match(score_policy_status.status)
    snapshot.assert_match(score_policy_status.loan)
