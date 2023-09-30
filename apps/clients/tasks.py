from apps.clients.models import Client
from apps.companies.models import Brand
from apps.upload_data.factories import UploadFileEventLogFactory
from apps.utils import types
from peoplecy_gowit import celery_app


@celery_app.task(soft_time_limit=10000)
def process_clients_raw_data(raw_data, operation_type, brand_id, upload_file_id):
    brand = Brand.objects.get(id=brand_id)
    try:
        created, updated, errors = Client.create_from_raw_data(raw_data=raw_data, operation_type='client', brand=brand)
        UploadFileEventLogFactory.success(upload_file_id, Client, types.ACTION_CREATE,
                                          f"Created: {len(created)} Updated: {len(updated)} Errors: {len(errors)}")
    except Exception as e:
        UploadFileEventLogFactory.error(upload_file_id, Client, types.ACTION_CREATE, str(e))
        raise e
