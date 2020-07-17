import pytest

from api.exceptions import ScoreError, TermError
from api.financial.rate import _default_normalize_score, _mount_data_frame, get_rate


def test_mount_df(snapshot):
    df = _mount_data_frame()
    terms = list(df.to_dict().keys())
    snapshot.assert_match(terms)


@pytest.mark.parametrize("score", [600, 679, 701, 831, 988, 1000])
def test_normalize_score(score, snapshot):
    snapshot.assert_match(_default_normalize_score(score))


@pytest.mark.parametrize("score", [10, 100, 300, 599, 1650])
def test_normalize_score_error(score):
    try:
        _default_normalize_score(score)
        assert False
    except ScoreError:
        assert True


@pytest.mark.parametrize("score, term", [(650, 6), (701, 12), (831, 9), (988, 6)])
def test_get_rate(score, term, snapshot):
    snapshot.assert_match(get_rate(score, term))


@pytest.mark.parametrize("term", [3, 15, 7])
def test_term_error(term):
    try:
        get_rate(900, term)
        assert False
    except TermError:
        assert True


@pytest.mark.parametrize("rate", [300, 100, 2000])
def test_rate_error(rate):
    try:
        get_rate(rate, 6)
        assert False
    except ScoreError:
        assert True
