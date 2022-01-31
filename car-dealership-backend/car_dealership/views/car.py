# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 31/01/2022

from car_dealership import models
from car_dealership.serializers.car import CarSerializer
from car_dealership.views import client
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

# returns the car object that contains the primary key equal to 'pk' or 404 if it doesn't exist
def get_object(pk):
    try:
        return models.Car.objects.get(pk=pk)
    except models.Car.DoesNotExist:
        raise Http404


# view to create a new car
class Car(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        response = {
            "error": "Bad request: " + str(serializer.errors),
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


# view to fetch, update and delete a car by ID
class CarByID(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        car = get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        response = {
            "error": "Bad request: " + str(serializer.errors),
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view to fetch all existing cars
class Cars(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        cars = models.Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


# view to buy a car
class CarBuy(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pkCar, pkClient, format=None):
        # validate user authority
        if request.user.id != pkClient:
            response = {
                "error": "Forbidden: user cannot take actions for other users",
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        car = get_object(pkCar)

        # check if the car does not already belong to someone else
        if car.id_client != None:
            response = {
                "error": "Bad request: this car already belongs to someone",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # updates the owner of the car
        car.id_client = client.get_object(pkClient)
        car.save()

        serializer = CarSerializer(car)
        return Response(serializer.data)


# view to sell a car
class CarSell(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        car = get_object(pk)

        # check if the car really belongs to someone
        if car.id_client == None:
            response = {
                "error": "Bad request: this car does not belong to anyone",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # validate user authority
        if request.user.id != car.id_client.id:
            response = {
                "error": "Forbidden: user cannot take actions for other users",
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        # updates the owner and state of the car
        car.id_client = None
        car.new = False
        car.save()

        serializer = CarSerializer(car)
        return Response(serializer.data)


# view to fetch all the cars that belong to a specified client
class CarsByClient(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pkClient, format=None):
        cars = models.Car.objects.filter(id_client=pkClient)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


# view to fetch all cars that have not yet been sold
class CarsNotSold(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        cars = models.Car.objects.filter(id_client=None)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
