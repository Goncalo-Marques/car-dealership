from os import name
from django.urls import path
from .views.index import index
from .views.client import account, signUp
from .views.car import newCars, usedCars, myCars

urlpatterns = [
    # index
    path("", index, name="index"),
    # client
    path("account/", account, name="account"),
    # TODO: client auth
    path("logIn/", account, name="logIn"),
    path("signUp/", signUp, name="signUp"),
    path("logOut/", account, name="logOut"),
    # car
    path("newCars/", newCars, name="newCars"),
    path("usedCars/", usedCars, name="usedCars"),
    path("myCars/", myCars, name="myCars"),
]
