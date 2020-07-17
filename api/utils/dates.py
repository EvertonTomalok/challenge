from datetime import date, datetime

from dateutil.relativedelta import relativedelta


def utc_string_to_datetime(date_string) -> datetime:
    return datetime.strptime(date_string, "%Y-%m-%d")


def get_age(date_str) -> int:
    """
    The date must to be in utc format yyyy-mm-dd
    :param date_str: str
    :return: int
    """
    born = utc_string_to_datetime(date_str)
    age = relativedelta(date.today(), born)
    return age.years


def is_older_then_18(date_str) -> bool:
    """
    The date must to be in utc format yyyy-mm-dd
    :param date_str: str
    :return: bool
    """
    return get_age(date_str) >= 18


def parse_str_to_date(date_str):
    """
    It parses some knowledge date formats to a Date object.
    :param date_str:
    :return: Date or None if is not possible to convert to Date Object
    """

    if isinstance(date_str, date):
        return date_str

    valid_formats = ("%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d")

    for fmt in valid_formats:
        try:
            dt_time = datetime.strptime(date_str, fmt)
            return date(dt_time.year, dt_time.month, dt_time.day)
        except ValueError:
            pass
    else:
        return None
