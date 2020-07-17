from os import getenv

from api.utils import (
    check_and_return_amount_float,
    check_and_return_term_int,
    is_cpf_valid,
    name_is_valid_field,
    normalize_cpf,
)
from api.utils.dates import parse_str_to_date

# These lambdas bellow will handle/check the fields received from api.
functions = {
    "name": lambda n: n if name_is_valid_field(n) else None,
    "cpf": lambda x: normalize_cpf(x) if is_cpf_valid(x) else None,
    "birthdate": lambda d: parse_str_to_date(d) if parse_str_to_date(d) else None,
    "amount": lambda a: check_and_return_amount_float(a)
    if check_and_return_amount_float(a)
    else None,
    "income": lambda i: check_and_return_amount_float(i)
    if check_and_return_amount_float(i)
    else None,
    "terms": lambda t: check_and_return_term_int(t)
    if check_and_return_term_int(t)
    else None,
}


def parse_loan_form(form):
    """
    Extract from the form the fields that will be send in the processing.
    :param form:
    :return:
    """
    name = form.get("name")
    cpf = form.get("cpf")

    return {
        "name": functions["name"](name),
        "cpf": normalize_cpf(cpf) if cpf else None,
        "birthdate": form.get("birthdate"),
        "amount": form.get("amount"),
        "terms": form.get("terms"),
        "income": form.get("income"),
    }


def check_loan_fields(fields):
    required_fields = list(functions.keys())
    invalid_fields = []

    # Checking for field required
    for field in required_fields:
        if not fields.get(field):
            invalid_fields.append({field: "Field is Required."})

    # Checking for invalid formats
    for field, field_value in fields.items():
        checking_format = functions.get(field)

        # The field required already was checked, so now we are going to check
        # the format.
        # If field is None, it wasn't send on form, and here it'll be passed
        if field_value and not checking_format(field_value):
            invalid_fields.append({field: "Invalid Format"})

    return invalid_fields


def is_api_key_valid(api_key: str) -> bool:
    """
    It'll check if the param is a valid key and the processing must to continue
    or the response 401 (Not allowed/Unauthorized will be send back)
    :param api_key: str
    :return: bool
    :raises: ValueError
    """
    api_key_env = getenv("API_KEY")

    if not api_key_env:
        raise ValueError("Api Key is not injected.")

    return api_key_env == api_key
