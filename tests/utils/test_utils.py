import pytest

from api.utils import (
    check_and_return_amount_float,
    check_and_return_term_int,
    is_cpf_valid,
    name_is_valid_field,
    normalize_cpf,
    transform_cpf,
)


def test_is_valid_cpf():
    assert is_cpf_valid("123.456.789-00")


@pytest.mark.parametrize("cpf", ["123.456.789-ab", "98765"])
def test_is_not_valid_cpf(cpf):
    assert not is_cpf_valid(cpf)


def test_normalize_cpf(snapshot):
    normalized = normalize_cpf("123.456.789-00")
    snapshot.assert_match(normalized)


@pytest.mark.parametrize("cpf", ["12345678900", "98765432111", "98076543244"])
def test_transform_cpf(cpf, snapshot):
    cpf_transformed = transform_cpf(cpf)
    snapshot.assert_match(cpf_transformed)


@pytest.mark.parametrize("cpf", ["123456789a0", "98765"])
def test_transform_cpf_error(cpf):
    """It'll raise ValueError"""
    try:
        transform_cpf(cpf)
        assert False
    except ValueError:
        assert True


def test_check_and_return_amount_float(snapshot):
    snapshot.assert_match(check_and_return_amount_float("1000.00"))


def test_not_check_and_return_amount_float():
    assert not check_and_return_amount_float("1000.abc")


def test_check_and_return_term_int(snapshot):
    snapshot.assert_match(check_and_return_term_int("6"))


def test_not_check_and_return_term_int():
    assert not check_and_return_amount_float("abc")


def test_name_is_valid_field():
    assert name_is_valid_field("abc")


@pytest.mark.parametrize("name", [123, ""])
def test_name_is_not_valid_field(name):
    assert not name_is_valid_field(name)
