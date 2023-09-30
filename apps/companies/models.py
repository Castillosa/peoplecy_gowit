from django.db import models

from apps.utils.models import BaseModel


# Create your models here.

class Company(models.Model):
    brand_name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='companies', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_name


class Sector(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()


# Create your models here.
class Brand(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/logos', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    subsector = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Component(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Attribute(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
