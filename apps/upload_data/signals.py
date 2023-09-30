from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.upload_data.models import UploadDataFile
from apps.utils import types
from apps.utils.helpers import check_value_in_tuple_list, debug
from apps.clients.tasks import process_clients_raw_data
from apps.operations.tasks import process_operations_raw_data


@receiver(post_save, sender=UploadDataFile)
def process_operation(sender, instance, created, **kwargs):
    debug("process_csv", instance.type)
    if check_value_in_tuple_list(instance.type, types.OPERATION_TYPE_CHOICES):
        if instance.raw_data:
            process_clients_raw_data.delay(instance.raw_data, instance.type, instance.brand_id, instance.id)
            process_operations_raw_data.delay(instance.raw_data, instance.type, instance.brand_id, instance.id)
