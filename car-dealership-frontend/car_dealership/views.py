import requests
from urllib.parse import urljoin
from django.shortcuts import render

BASE_URL = "http://127.0.0.1:8000/"


def index(request):
    return render(request, "index.html", None)


def clients(request):
    # get the list of clients
    response = requests.get(urljoin(BASE_URL, "clients/"))
    # transform the response to json objects
    clients = response.json()
    return render(request, "clients.html", {"clients": clients})


def cars(request):
    # get the list of cars
    response = requests.get(urljoin(BASE_URL, "cars/"))
    # transform the response to json objects
    cars = response.json()
    for car in cars:
        print(car["new"])

    return render(request, "cars.html", {"cars": cars})
