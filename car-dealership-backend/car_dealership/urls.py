from django.urls import path
from car_dealership.views.client import *
from car_dealership.views.brand import *


urlpatterns = [
    path('clients/', ClientList.as_view()),
    path('client/<int:pk>/', ClientDetail.as_view()),

    path('brands/', BrandList.as_view()),
    path('brand/<int:pk>/', BrandDetail.as_view()),
]