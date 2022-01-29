from django.shortcuts import render
from .consts import TEMPLATE_CARS, TEMPLATE_ERROR, TEMPLATE_MY_CARS
from . import helpers


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
