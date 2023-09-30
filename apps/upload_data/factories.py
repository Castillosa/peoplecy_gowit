from apps.upload_data import tasks
from apps.utils import types


class UploadFileEventLogFactory:

    @staticmethod
    def success(upload_file_id, log_event_class, action, message=None):
        tasks.add_log_to_upload_file.delay(upload_file_id,
                                           types.LOG_TYPE_SUCCESS,
                                           log_event_class.__name__,
                                           action,
                                           message)

    @staticmethod
    def error(upload_file_id, log_event_class, action, message=None):
        tasks.add_log_to_upload_file.delay(upload_file_id,
                                           types.LOG_TYPE_ERROR,
                                           log_event_class.__name__,
                                           action,
                                           message)

    @staticmethod
    def warning(upload_file_id, log_event_class, action, message=None):
        tasks.add_log_to_upload_file.delay(upload_file_id,
                                           types.LOG_TYPE_WARNING,
                                           log_event_class.__name__,
                                           action,
                                           message)

    @staticmethod
    def info(upload_file_id, log_event_class, action, message=None):
        tasks.add_log_to_upload_file.delay(upload_file_id,
                                           types.LOG_TYPE_INFO,
                                           log_event_class.__name__,
                                           action,
                                           message)
