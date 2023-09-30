from datetime import datetime

from django.db import models

from apps.utils import types
from apps.utils.models import BaseModel, RawDataImportable, BaseCsvColumnEquivalence, BaseCsvValueEquivalence
from django.utils.translation import gettext_lazy as _, get_language


# Create your models here.
class OperationType(BaseModel):
    brand = models.ForeignKey('companies.Brand', on_delete=models.SET_NULL, related_name='operation_types', null=True,
                              blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    priority = models.IntegerField(default=0)
    id_name = models.CharField(max_length=100, null=True, blank=True)
    def get_translated_string(self):
        try:
            active_language = get_language()
            return self.translations.get(operation_type=self.id, language=active_language).name
        except OperationTypeI18n.DoesNotExist:
            return self.name

    def __str__(self):
        return self.name


class OperationTypeI18n(BaseModel):
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10, choices=types.LANGUAGE_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class OperationCsvColumnEquivalence(BaseCsvColumnEquivalence):
    def __init__(self, *args, **kwargs):
        super(OperationCsvColumnEquivalence, self).__init__(Operation, *args, **kwargs)


class OperationCsvValueEquivalence(BaseCsvValueEquivalence):
    def __init__(self, *args, **kwargs):
        super(OperationCsvValueEquivalence, self).__init__(Operation, *args, **kwargs)


class Operation(BaseModel, RawDataImportable):
    brand = models.ForeignKey('companies.Brand', on_delete=models.SET_NULL, related_name='operations', null=True,
                              blank=True)
    date = models.DateField(null=True, blank=True)
    internal_id = models.CharField(max_length=100, null=True, blank=True)
    internal_client_id = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True, choices=types.OPERATION_TYPE_CHOICES)
    operation_status = models.CharField(max_length=50, null=True, blank=True)
    linked_operation = models.ForeignKey('Operation', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    need = models.TextField(null=True, blank=True)
    motivation = models.TextField(null=True, blank=True)
    vehicle_type = models.CharField(max_length=50, null=True, blank=True)
    product = models.CharField(max_length=100, null=True, blank=True)
    professional = models.CharField(max_length=50, null=True, blank=True)
    technician = models.CharField(max_length=50, null=True, blank=True)
    assistant = models.CharField(max_length=50, null=True, blank=True)
    administrative = models.CharField(max_length=50, null=True, blank=True)
    advisor = models.CharField(max_length=50, null=True, blank=True)
    carrier = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    zone = models.CharField(max_length=50, null=True, blank=True)
    delegation = models.CharField(max_length=50, null=True, blank=True)
    sales_center = models.CharField(max_length=50, null=True, blank=True)
    technical_center = models.CharField(max_length=50, null=True, blank=True)
    channel = models.CharField(max_length=50, null=True, blank=True)
    distributor = models.CharField(max_length=50, null=True, blank=True)
    supplier = models.CharField(max_length=50, null=True, blank=True)
    logistics = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)

    column_equivalence_class = OperationCsvColumnEquivalence
    value_equivalence_class = OperationCsvValueEquivalence
