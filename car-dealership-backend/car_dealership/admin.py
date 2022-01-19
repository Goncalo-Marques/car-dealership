from django.contrib import admin
from . import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "birthdate")


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "id_client")
