from datetime import date

import pytest

from api.utils.dates import get_age, is_older_then_18, parse_str_to_date


@pytest.mark.parametrize("date", ["15/08/1992", "1992-08-15", "1992/08/15"])
def test_parse_str_to_date(date, snapshot):
    snapshot.assert_match(parse_str_to_date(date))


def test_parse_str_to_date_date_obj(snapshot):
    snapshot.assert_match(parse_str_to_date(date(1992, 8, 15)))


def test_parse_str_to_date_raise_value_error():
    assert not parse_str_to_date("19920815")


@pytest.mark.parametrize("d", ["1992-08-15", "2005-08-15", "2010-08-15"])
def test_get_age(d, snapshot):
    snapshot.assert_match(get_age(d))


@pytest.mark.parametrize("dt", ["1992-08-15", "2005-08-15", "2010-08-15"])
def test_is_older(dt, snapshot):
    snapshot.assert_match(is_older_then_18(dt))
