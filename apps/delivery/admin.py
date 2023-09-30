from django.contrib import admin

from apps.delivery.forms import DeliveryConfigForm
# Register your models here.
from apps.delivery.models import DeliveryInterval, SurveyDeliveryConfig, DeliveryRecord, DeliveryConfig

@admin.register(DeliveryInterval)
class DeliveryIntervalAdmin(admin.ModelAdmin):
    pass

@admin.register(DeliveryConfig)
class DeliveryConfigAdmin(admin.ModelAdmin):
    form = DeliveryConfigForm

@admin.register(DeliveryRecord)
class DeliveryRecordAdmin(admin.ModelAdmin):
    pass
