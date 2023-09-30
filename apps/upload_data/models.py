from django.db import models

from apps.companies.models import Company
from apps.upload_data.helpers import extract_csv
from apps.utils import types
from django.utils import timezone

from apps.utils.models import BaseModel


class UploadDataFile(BaseModel):
    brand = models.ForeignKey('companies.Brand', on_delete=models.SET_NULL, related_name='data_files', null=True,
                              blank=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)
    raw_data = models.TextField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    TYPE_CHOICES = types.FILE_TYPE_CHOICES
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    error = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True, blank=True)

    def process_csv(self):
        csv_path = self.file.path

        headers, data = extract_csv(csv_path)

        print(headers)
        print(data)

        self.processed = True
        self.processed_at = timezone.now()


class UploadDataFileEventLog(BaseModel):
    uploadDataFile = models.ForeignKey(UploadDataFile, on_delete=models.CASCADE, related_name='logs')
    log_type = models.CharField(max_length=100, choices=types.LOG_TYPE_CHOICES)
    log_event_class = models.CharField(max_length=100)
    action = models.CharField(max_length=100, choices=types.ACTION_CHOICES)
    message = models.TextField(null=True, blank=True)


    @classmethod
    def create(cls, uploadDataFile_id, log_type, log_event_class, action, message=None):
        log = cls()
        log.uploadDataFile_id = uploadDataFile_id
        log.log_type = log_type
        log.log_event_class = log_event_class
        log.action = action
        log.message = message
        log.save()

        return log
