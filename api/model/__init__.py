from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import DateType, DecimalType, IntType, StringType

from api.model.utils import generate_uuid
from api.utils.enumerators import ProcessingStatus


def is_inside(value):
    if int(value) not in [6, 9, 12]:
        raise ValidationError("The terms not in [6, 9, 12]")
    return value


def is_between(value):
    if not 1000 <= value <= 4000:
        raise ValidationError("The amount must to be between 1000.00 - 4000.00")
    return value


class Client(Model):
    _id = StringType(default=generate_uuid())
    name = StringType(required=True, min_length=1, max_length=80)
    cpf = StringType(required=True, min_length=11, max_length=11)
    birthdate = DateType(required=True)
    amount = DecimalType(required=True, validators=[is_between])
    terms = IntType(required=True, validators=[is_inside])
    income = DecimalType(required=True)


class Loan(Model):
    _id = StringType(required=True)
    status = StringType(default=ProcessingStatus.processing.value)
    result = StringType()
    refused_policy = StringType()
    amount = DecimalType(min_value=1000, max_value=4000, validators=[is_between])
    terms = IntType(min_value=6, max_value=12, validators=[is_inside])
