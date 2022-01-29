from os import name
from django.urls import path
from .views.index import index
from .views.client import account, logIn, signUp, logOut
from .views.car import newCars, usedCars, myCars

urlpatterns = [
    # index
    path("", index, name="index"),
    # client
    path("account/", account, name="account"),
    path("logIn/", logIn, name="logIn"),
    path("signUp/", signUp, name="signUp"),
    path("logOut/", logOut, name="logOut"),
    # car
    path("newCars/", newCars, name="newCars"),
    path("usedCars/", usedCars, name="usedCars"),
    path("myCars/", myCars, name="myCars"),
]
