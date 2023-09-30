from django.contrib import admin

from apps.upload_data.models import UploadDataFile, UploadDataFileEventLog


class EventLogInline(admin.TabularInline):
    model = UploadDataFileEventLog
    readonly_fields = ('log_type', 'log_event_class', 'action', 'message', 'created_at')
    extra = 0
    ordering = ('-created_at',)


@admin.register(UploadDataFile)
class UploadDataAdmin(admin.ModelAdmin):
    inlines = [
        EventLogInline,
    ]
