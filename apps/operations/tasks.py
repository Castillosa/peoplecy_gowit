from peoplecy_gowit import celery_app
from .models import Operation
from apps.companies.models import Brand
from apps.upload_data.models import UploadDataFile
from apps.upload_data.factories import UploadFileEventLogFactory
from ..utils import types


@celery_app.task(soft_time_limit=10000)
def process_operations_raw_data(raw_data, operation_type, brand_id, upload_file_id):
    brand = Brand.objects.get(id=brand_id)
    try:
        created, updated, errors = Operation.create_from_raw_data(raw_data=raw_data, operation_type=operation_type, brand=brand)
        UploadFileEventLogFactory.success(upload_file_id, Operation, types.ACTION_CREATE, f"Created: {len(created)} Updated: {len(updated)} Errors: {len(errors)}")
    except Exception as e:
        UploadFileEventLogFactory.error(upload_file_id, Operation, types.ACTION_CREATE, str(e))
        raise e
