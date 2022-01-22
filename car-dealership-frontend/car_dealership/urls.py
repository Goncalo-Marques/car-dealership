from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("account/", views.account, name="account/"),

    path("clients/", views.clients, name="clients"),
    path("cars/", views.cars, name="cars"),
]
