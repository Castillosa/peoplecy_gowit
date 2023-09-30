from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OperationCsvColumnEquivalence, OperationType, OperationTypeI18n
from apps.utils.helpers import debug
from ..companies.models import Brand
from ..utils.types import OPERATION_TYPE_CHOICES


def only_one_id_column_equivalence(sender, instance, **kwargs):
    debug(str(sender) + ' Post_save_signal:', "is_id_value")
    if instance.is_id_value:
        instance.clean_is_id_value()


def create_operation_types(sender, instance, created, **kwargs):
    if created:
        for operation_type_choice in OPERATION_TYPE_CHOICES:
            operation_type = OperationType.objects.create(name=operation_type_choice[1], id_name=operation_type_choice[0], brand=instance)
            OperationTypeI18n.objects.create(operation_type=operation_type, language='en', name=operation_type_choice[0])


post_save.connect(only_one_id_column_equivalence, sender=OperationCsvColumnEquivalence)
post_save.connect(create_operation_types, sender=Brand)
