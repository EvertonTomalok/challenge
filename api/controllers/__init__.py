import json
import logging
from collections import namedtuple
from os import getenv
from random import randint, random

import backoff
import requests

logger = logging.getLogger()

api_key = getenv("API_KEY")

DefaultValues = namedtuple("DefaultValues", "score commitment")


@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.Timeout, requests.exceptions.ConnectionError),
    max_tries=3,
    max_time=300,
)
def get_url(url: str, method: str, payload=None, headers=None):
    payload = payload or {}
    response = requests.request(method, url, headers=headers, data=json.dumps(payload))
    return response


def get_score(cpf: str) -> int:
    default_value = default_cpf_values.get(cpf)
    if default_value:
        return default_value.score
    return randint(300, 1000)


def get_commitment(cpf: str) -> float:
    default_value = default_cpf_values.get(cpf)
    if default_value:
        return default_value.commitment
    return random()


# Just to be easier testing
default_cpf_values = {
    "12345678900": DefaultValues(131, 0.9),
    "12345678901": DefaultValues(900, 0.1),
}
