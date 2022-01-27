import requests
from urllib.parse import urljoin
from django.shortcuts import render
from .consts import *


def newCars(request):
    # get the list of cars
    response = requests.get(urljoin(BASE_URL, "carsNotSold/"))

    # transform the response to json object
    tempCars = response.json()

    # get all new cars
    cars = []
    for car in tempCars:
        # checks if the car is new
        if car["new"] == True:
            cars.append(car)

    # TODO: client auth
    context = {
        "title": "New Cars",
        "client": requests.get(urljoin(BASE_URL, "client/1/")).json(),
        "cars": cars,
    }
    return render(request, "cars.html", context)


def usedCars(request):
    # get the list of cars
    response = requests.get(urljoin(BASE_URL, "carsNotSold/"))

    # transform the response to json object
    tempCars = response.json()

    # get all used cars
    cars = []
    for car in tempCars:
        # checks if the car is not new
        if car["new"] == False:
            cars.append(car)

    # TODO: client auth
    context = {
        "title": "Used Cars",
        "client": requests.get(urljoin(BASE_URL, "client/1/")).json(),
        "cars": cars,
    }
    return render(request, "cars.html", context)


def myCars(request):
    # get cars by client
    response = requests.get(urljoin(BASE_URL, "carsByClient/1/"))

    # transform the response to json object
    cars = response.json()

    # TODO: client auth
    context = {
        "client": None,
        "cars": cars,
    }
    return render(request, "myCars.html", context)
