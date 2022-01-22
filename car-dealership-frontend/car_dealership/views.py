import requests
from urllib.parse import urljoin
from django.shortcuts import render

# API base url
BASE_URL = "http://127.0.0.1:8000/"

# maximum number of featured cars
MAX_FEATURED_CARS = 5


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

    context = {
        "client": None,
        "featured": featuredCars,
        "cars": otherCars,
    }
    return render(request, "index.html", context)


def account(request):
    # get client
    response = requests.get(urljoin(BASE_URL, "client/1/"))

    # transform the response to json object
    client = response.json()
    return render(request, "account.html", {"client": client})


def clients(request):
    # get the list of clients
    response = requests.get(urljoin(BASE_URL, "clients/"))

    # transform the response to json object
    clients = response.json()
    return render(request, "clients.html", {"clients": clients})


def cars(request):
    # get the list of cars
    response = requests.get(urljoin(BASE_URL, "cars/"))

    # transform the response to json object
    cars = response.json()
    for car in cars:
        print(car["new"])

    return render(request, "cars.html", {"cars": cars})
