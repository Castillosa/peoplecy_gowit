from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models

from apps.operations.models import OperationCsvColumnEquivalence, OperationCsvValueEquivalence, Operation
from apps.utils.models import BaseModel, BaseCsvColumnEquivalence, BaseCsvValueEquivalence, RawDataImportable



class Client(BaseModel, RawDataImportable):
    brand = models.ForeignKey('companies.Brand', on_delete=models.SET_NULL, related_name='clients', null=True,
                              blank=True)
    internal_id = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    crm_url = models.URLField(null=True, blank=True)
    dni = models.CharField(max_length=20, null=True, blank=True)
    contact_notes = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    age_range = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    importance = models.CharField(max_length=20, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)
    value = models.CharField(max_length=20, null=True, blank=True)

    column_equivalence_class = OperationCsvColumnEquivalence
    value_equivalence_class = OperationCsvValueEquivalence

    def save(self, *args, **kwargs):
        if self.phone:
            self.phone = self.phone.split('/')[0]
        super(Client, self).save(*args, **kwargs)

    def clean(self):
        if not self.email and not self.phone:
            raise ValidationError("Debes proporcionar al menos un correo electrónico o un número de teléfono.")

