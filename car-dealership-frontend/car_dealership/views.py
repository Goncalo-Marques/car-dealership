import requests
from django.shortcuts import render

def clients(request):
   # get the list of clients
   response = requests.get('http://127.0.0.1:8000/clients/')
   # transform the response to json objects
   clients = response.json()
   return render(request, "clients.html", {"clients": clients})

def cars(request):
   # get the list of cars
   response = requests.get('http://127.0.0.1:8000/cars/')
   # transform the response to json objects
   cars = response.json()
   return render(request, "cars.html", {"cars": cars})