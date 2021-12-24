from django.urls import path
from car_dealership.views.client import *
from car_dealership.views.brand import *

urlpatterns = [
    path('client/',  Client.as_view()),
    path('client/<int:pk>/', ClientByID.as_view()),
    path('clients/', Clients.as_view()),

    path('brand/', Brand.as_view()),
    path('brand/<pk>', BrandByName.as_view()),
    path('brands/', Brands.as_view()),
]