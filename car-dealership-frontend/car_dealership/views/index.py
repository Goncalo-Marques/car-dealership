# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 29/01/2022

from django.shortcuts import render
from .consts import MAX_FEATURED_CARS, TEMPLATE_ERROR, TEMPLATE_INDEX
from . import helpers

# index view
def index(request):
    # get the list of cars not sold
    response = helpers.get("carsNotSold/", request.COOKIES)
    if response.status_code != 200:
        return render(request, TEMPLATE_ERROR, response.json())

    # transform the response to json object
    cars = response.json()

    # featured cars
    featuredCars = []
    featuredCount = 0

    # other cars
    otherCars = []

    for car in cars:
        # checks if the car belongs to the featured category
        if car["new"] == True and featuredCount < MAX_FEATURED_CARS:
            featuredCars.append(car)
            featuredCount += 1
        else:
            otherCars.append(car)

    context = {
        "client": helpers.get_client_or_none(request),
        "featured": featuredCars,
        "cars": otherCars,
    }
    return render(request, TEMPLATE_INDEX, context)
