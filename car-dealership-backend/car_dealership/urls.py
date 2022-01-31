# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 31/01/2022

from django.urls import path, re_path
from car_dealership.views.auth import *
from car_dealership.views.client import *
from car_dealership.views.brand import *
from car_dealership.views.car import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Car Dealership API",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    # docs https://drf-yasg.readthedocs.io/en/stable/readme.html#installation
    re_path(
        "^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        "^docs/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    # auth
    path("auth/login/", Login.as_view()),
    path("auth/register/", Register.as_view()),
    path("auth/logout/", Logout.as_view()),
    # client
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
