from peoplecy_gowit import celery_app
from .models import UploadDataFileEventLog
from apps.upload_data.models import UploadDataFile


@celery_app.task()
def add_log_to_upload_file(upload_file_id, log_type, log_event_class, action, message):
    UploadDataFileEventLog.create(uploadDataFile_id=upload_file_id,
                                  log_type=log_type,
                                  log_event_class=log_event_class,
                                  action=action,
                                  message=message)
