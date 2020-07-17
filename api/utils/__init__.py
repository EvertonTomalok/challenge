from typing import Any


def is_cpf_valid(cpf_str):
    """
    It checks if the cpf is only number and has length 11
    :param cpf_str: str
    :return: bool
    """

    cpf_str = normalize_cpf(cpf_str)

    try:
        int(cpf_str)
    except ValueError:
        return False

    if len(cpf_str) != 11:
        return False

    return True


def normalize_cpf(cpf_str: str) -> str:
    """
    It'll transform the cpf format 123.456.789-00 to 12345678900
    :param cpf_str: str
    :return: str
    """
    return cpf_str.replace(".", "").replace("-", "")


def transform_cpf(cpf_str: str) -> str:
    """
    It'll transform a cpf in the format 12345678900 to 123.456.789-00
    :param cpf_str: str
    :return: str
    :raises: ValueError
    """

    # Checking if CPF is only number
    int(cpf_str)

    if len(cpf_str) != 11:
        raise ValueError(
            "The format of CPF is invalid, it must be only number, " "like 12345678900"
        )

    return f"{cpf_str[0:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:11]}"


def check_and_return_amount_float(amount: Any):
    """
    It will check if the amount value is valid
    :param amount: Any
    :return: float or None if the value is invalid
    """

    try:
        return float(amount)
    except ValueError:
        return None


def check_and_return_term_int(terms: Any):
    """
    It will check if the amount value is valid
    :param terms: Any
    :return: int or None if the value is invalid
    """

    try:
        return int(terms)
    except ValueError:
        return None


def name_is_valid_field(name_str: str) -> bool:
    if not isinstance(name_str, str) or name_str == "":
        return False
    return True
