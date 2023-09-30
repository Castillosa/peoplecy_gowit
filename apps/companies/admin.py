from django.contrib import admin

from apps.companies.models import Company, Component, Attribute, Brand


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'legal_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('brand_name', 'legal_name')


# class ComponentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'long_name', 'is_active')
#     list_filter = ('company', 'is_active')
#     search_fields = ('name', 'long_name')


# class AttributeAdmin(admin.ModelAdmin):
#     list_display = ('component', 'name', 'long_name', 'is_active')
#     list_filter = ('component', 'is_active')
#     search_fields = ('name', 'long_name')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'logo', 'website', 'category', 'sector', 'subsector')
    list_filter = ('company', 'sector')
    search_fields = ('name', 'category', 'subsector')


admin.site.register(Company, CompanyAdmin)
# admin.site.register(Component, ComponentAdmin)
# admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Brand, BrandAdmin)
