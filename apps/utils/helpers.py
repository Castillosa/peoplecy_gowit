import unidecode
from django.db import models

from django.conf import settings

from apps.utils import types


def normalize_str(text):
    normalized_str = unidecode.unidecode(text)
    return normalized_str.lower()


def equal_str(str1, str2):
    str1 = normalize_str(str1)
    str2 = normalize_str(str2)

    return str1 == str2


def get_fields_as_choices(model):
    return [
        (field.name, field.verbose_name) for field in model._meta.get_fields() if
        isinstance(field, (models.CharField, models.IntegerField, models.DateField)) and field.name != "id"
    ]


def debug(header, value):
    if settings.DEBUG:
        print(header, ": ", value)


def check_value_in_tuple_list(value, tuple):
    debug("check_value_in_tuple_list", value)
    for key, val in tuple:
        if key == value:
            return True
