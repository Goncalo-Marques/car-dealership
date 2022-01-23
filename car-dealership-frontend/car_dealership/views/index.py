import requests
from urllib.parse import urljoin
from django.shortcuts import render
from .consts import *


def index(request):
    # get the list of cars not sold
    response = requests.get(urljoin(BASE_URL, "carsNotSold/"))

    # transform the response to json object
    cars = response.json()

    # featured cars
    featuredCars = []
    featuredCount = 0

    # other cars
    otherCars = []

    for car in cars:
        # checks if the car belongs to the featured category
        if car["new"] == True and featuredCount < 5:
            featuredCars.append(car)
            featuredCount += 1
        else:
            otherCars.append(car)

    # TODO: client auth
    context = {
        "client": requests.get(urljoin(BASE_URL, "client/1/")).json(),
        "featured": featuredCars,
        "cars": otherCars,
    }
    return render(request, "index.html", context)
