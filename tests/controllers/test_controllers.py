import responses
import pytest
import random

from api.controllers import get_commitment, get_score, get_url


@responses.activate
def test_get_url(snapshot):
    url = "http://example.com"
    method = "GET"

    responses.add(
        responses.Response(method=method, url=url, status=200, json={"test": 123})
    )

    res = get_url(url, method)

    snapshot.assert_match(res.json())


@pytest.mark.parametrize("cpf", ["12345678900", "12345678912"])
def test_get_score(cpf, snapshot):
    random.seed(0)
    score = get_score(cpf)
    snapshot.assert_match(score)


@pytest.mark.parametrize("cpf", ["12345678900", "12345678912"])
def test_get_commitment(cpf, snapshot):
    random.seed(0)
    commitment = get_commitment(cpf)
    snapshot.assert_match(commitment)
