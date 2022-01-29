from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from . import models

# custom admin page for Brand
@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# custom admin page for Client
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "view_cars_link")
    search_fields = ("full_name",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def view_cars_link(self, obj):
        url = (
            reverse("admin:car_dealership_car_changelist")
            + "?"
            + urlencode({"id_client": f"{obj.id}"})
        )

        # number of cars owned by the client
        count = obj.car_set.count()
        return format_html('<a href="{}">{} Car(s)</a>', url, count)

    view_cars_link.short_description = "cars"


# custom admin page for Car
@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "view_client_link")
    search_fields = ("name",)
    list_filter = ("id_client",)

    def view_client_link(self, obj):
        if obj.id_client == None:
            return None

        url = reverse("admin:car_dealership_client_change", args=[obj.id_client.id])

        # name of the client that owns the car
        clientName = obj.id_client
        return format_html('<a href="{}">{}</a>', url, clientName)

    view_client_link.short_description = "client"
