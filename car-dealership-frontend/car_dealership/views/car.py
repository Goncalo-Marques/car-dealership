# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 29/01/2022

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import helpers
from .consts import (
    TEMPLATE_CARS,
    TEMPLATE_ERROR,
    TEMPLATE_MY_CARS,
    URL_INDEX,
    URL_MY_CARS,
)

# new cars view
def newCars(request):
    # get the list of cars not sold
    response = helpers.get("carsNotSold/", request.COOKIES)
    if response.status_code != 200:
        return render(request, TEMPLATE_ERROR, response.json())

    # transform the response to json object
    tempCars = response.json()

    # get all new cars
    cars = []
    for car in tempCars:
        # checks if the car is new
        if car["new"] == True:
            cars.append(car)

    context = {
        "title": "New Cars",
        "client": helpers.get_client_or_none(request),
        "cars": cars,
    }
    return render(request, TEMPLATE_CARS, context)


# used cars view
def usedCars(request):
    # get the list of cars not sold
    response = helpers.get("carsNotSold/", request.COOKIES)
    if response.status_code != 200:
        return render(request, TEMPLATE_ERROR, response.json())

    # transform the response to json object
    tempCars = response.json()

    # get all used cars
    cars = []
    for car in tempCars:
        # checks if the car is not new
        if car["new"] == False:
            cars.append(car)

    context = {
        "title": "Used Cars",
        "client": helpers.get_client_or_none(request),
        "cars": cars,
    }
    return render(request, TEMPLATE_CARS, context)


# client cars view
def myCars(request):
    client = helpers.get_client_or_none(request)
    cars = None

    if client != None:
        # get cars by client
        clientID = client.get("id", None)
        response = helpers.get(f"carsByClient/{clientID}/", request.COOKIES)
        if response.status_code != 200:
            return render(request, TEMPLATE_ERROR, response.json())

        # transform the response to json object
        cars = response.json()

    context = {
        "client": client,
        "cars": cars,
    }
    return render(request, TEMPLATE_MY_CARS, context)


# view to buy a car
def buyCar(request, pkCar):
    client = helpers.get_client_or_none(request)
    clientID = client.get("id", None)

    response = helpers.get(f"buyCar/{pkCar}/{clientID}/", request.COOKIES)
    if response.status_code != 200:
        return render(request, TEMPLATE_ERROR, response.json())

    return HttpResponseRedirect(reverse(URL_INDEX))


# view to sell a car
def sellCar(request, pkCar):
    response = helpers.get(f"sellCar/{pkCar}/", request.COOKIES)
    if response.status_code != 200:
        return render(request, TEMPLATE_ERROR, response.json())

    return HttpResponseRedirect(reverse(URL_MY_CARS))
