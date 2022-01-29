# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 29/01/2022

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("car_dealership.urls")),
]
