from os import name
from django.urls import path
from . import views

urlpatterns = [
    # index
    path("", views.index, name="index"),
    # client
    path("account/", views.account, name="account"),
    path("logIn/", views.account, name="logIn"),
    path("signUp/", views.account, name="signUp"),
    path("logOut/", views.account, name="logOut"),
    path("clients/", views.clients, name="clients"),
    # car
    path("newCars/", views.cars, name="newCars"),
    path("usedCars/", views.cars, name="usedCars"),
    path("myCars/", views.myCars, name="myCars"),
]
