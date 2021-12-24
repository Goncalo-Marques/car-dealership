from django.urls import path
from car_dealership.views.client import *
from car_dealership.views.brand import *

urlpatterns = [
    # client
    path("client/", Client.as_view()),
    path("client/<int:pk>/", ClientByID.as_view()),
    path("clients/", Clients.as_view()),
    # brand
    path("brand/", Brand.as_view()),
    path("brand/<str:pk>", BrandByName.as_view()),
    path("brands/", Brands.as_view()),
]
