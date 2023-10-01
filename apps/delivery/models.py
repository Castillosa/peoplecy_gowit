from dateutil.utils import today
from django.db import models

from apps.utils.models import BaseModel
from apps.utils.types import OPERATION_TYPE_CHOICES, INTERVAL_CHOICES


class DeliveryInterval(BaseModel):
    brand = models.ForeignKey("companies.Brand", on_delete=models.CASCADE)
    number = models.IntegerField()
    interval = models.CharField(max_length=50, choices=INTERVAL_CHOICES)


class SurveyDeliveryConfig(BaseModel):
    brand = models.ForeignKey("companies.Brand", on_delete=models.CASCADE)
    last_available_operation_date = models.DateField(null=True, blank=True)
    operation_type = models.ForeignKey("operations.OperationType", on_delete=models.CASCADE, null=True, blank=True)
    delivery_start_date = models.DateField(null=True, blank=True)
    reminder_interval = models.ForeignKey(DeliveryInterval, on_delete=models.SET_NULL, null=True, blank=True,
                                          related_name="survey_delivery_reminder_interval")
    reminder_max_tries = models.IntegerField(null=True, blank=True)
    response_time_limit_interval = models.ForeignKey(DeliveryInterval, on_delete=models.SET_NULL, null=True, blank=True,
                                                     related_name="survey_delivery_response_time_limit_interval")
    incubation_interval = models.ForeignKey(DeliveryInterval, on_delete=models.SET_NULL, null=True, blank=True,
                                            related_name="survey_delivery_incubation_interval")
    survey = models.ForeignKey("surveys.Survey", on_delete=models.CASCADE, null=True, blank=True)
    METHOD_CHOICES = (
        ("email", "Email"),
        ("sms", "SMS"),
        ('available', 'Available'),
    )
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

class DeliveryContentTemplate(BaseModel):
    pass


class DeliveryConfig(BaseModel):
    survey = models.ForeignKey("surveys.Survey", on_delete=models.CASCADE)
    brand = models.ForeignKey("companies.Brand", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    operation_type = models.ForeignKey("operations.OperationType", on_delete=models.CASCADE, null=True, blank=True)
    delivery_hour = models.TimeField(null=True, blank=True)
    delivery_days = models.CharField(max_length=100, null=True, blank=True)
    repeat = models.BooleanField(default=False)
    repeat_interval_value = models.IntegerField(null=True, blank=True)
    INTERNAL_BLOCK_CHOICES = (
        ('', '----'),
        ('w', 'Semanas'),
        ('m', 'Meses'),
        ('y', 'Años'),
    )
    repeat_interval_type = models.CharField(max_length=100, choices=INTERNAL_BLOCK_CHOICES, null=True, blank=True)
    METHOD_CHOICES = (
        ("email", "Email"),
        ("sms", "SMS"),
        ('both', 'Both')
    )
    content_template = models.ForeignKey(DeliveryContentTemplate, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    reminder = models.BooleanField(default=False)
    reminder_in_days = models.IntegerField(null=True, blank=True) # can be a zero because hour, days are not 24h is only a day of the month
    reminder_deliver_hour = models.TimeField(null=True, blank=True)
    reminder_deliver_days = models.CharField(max_length=100, null=True, blank=True)
    reminder_max_tries = models.IntegerField(null=True, blank=True)
    reminder_retry_in_days = models.IntegerField(null=True, blank=True)
    answer_time_limit = models.IntegerField(null=True, blank=True)
    max_valid_operation_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    ## Todo: configurar textos email y sms


class DeliveryRecord(BaseModel):
    config = models.ForeignKey(SurveyDeliveryConfig, on_delete=models.CASCADE)
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    operation_type = models.ForeignKey("operations.OperationType", on_delete=models.CASCADE, null=True, blank=True)
    send_date = models.DateTimeField(null=True, blank=True)
    start_response_date = models.DateTimeField(null=True, blank=True)
    finish_response_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
