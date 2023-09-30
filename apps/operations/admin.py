from django.contrib import admin

from .models import Operation, OperationCsvColumnEquivalence, OperationCsvValueEquivalence, OperationType, \
    OperationTypeI18n


# Register your models here.

class OperationAdminI18nInline(admin.TabularInline):
    model = OperationTypeI18n
    extra = 1


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['date', 'internal_client_id', 'type', 'operation_status', 'linked_operation', 'amount']
    search_fields = ['internal_client_id']


@admin.register(OperationCsvColumnEquivalence)
class OperationCsvEquivalenceAdmin(admin.ModelAdmin):
    list_display = ['brand', 'column', 'equivalence', 'operation_type']


@admin.register(OperationCsvValueEquivalence)
class EmployeeCsvValueEquivalenceAdmin(admin.ModelAdmin):
    list_display = ['column', 'value', 'equivalence']


@admin.register(OperationTypeI18n)
class OperationTypeI18nAdmin(admin.ModelAdmin):
    list_display = ['name', 'operation_type', 'language']
    search_fields = ['name', ]
    list_filter = ['language', 'operation_type']


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand']
    search_fields = ['name', 'brand']
    list_filter = ['brand']
    inlines = [OperationAdminI18nInline]
