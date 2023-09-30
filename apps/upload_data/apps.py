from django.apps import AppConfig


class UploadFilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.upload_data"

    def ready(self):
        from . import signals
