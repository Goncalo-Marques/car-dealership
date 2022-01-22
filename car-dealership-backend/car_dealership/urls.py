from django.urls import path
from car_dealership.views.client import *
from car_dealership.views.brand import *
from car_dealership.views.car import *

urlpatterns = [
    # client
    path("client/", Client.as_view()),
    path("client/<int:pk>/", ClientByID.as_view()),
    path("clients/", Clients.as_view()),
    # brand
    path("brand/", Brand.as_view()),
    path("brand/<str:pk>/", BrandByName.as_view()),
    path("brands/", Brands.as_view()),
    # car
    path("car/", Car.as_view()),
    path("car/<int:pk>/", CarByID.as_view()),
    path("cars/", Cars.as_view()),
    path("buyCar/<int:pkCar>/<int:pkClient>/", CarBuy.as_view()),
    path("sellCar/<int:pk>/", CarSell.as_view()),
    path("carsByClient/<int:pkClient>/", CarsByClient.as_view()),
    path("carsNotSold/", CarsNotSold.as_view()),
]
