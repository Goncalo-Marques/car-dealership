from django.http.response import HttpResponseBadRequest
from car_dealership import models
from car_dealership.serializers.car import CarSerializer
from car_dealership.views import client
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def get_object(pk):
    try:
        return models.Car.objects.get(pk=pk)
    except models.Car.DoesNotExist:
        raise Http404


class Car(APIView):
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarByID(APIView):
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Cars(APIView):
    def get(self, request, format=None):
        cars = models.Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class CarBuy(APIView):
    def get(self, request, pkCar, pkClient, format=None):
        car = get_object(pkCar)
        if car.id_client != None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        car.id_client = client.get_object(pkClient)
        car.save()

        serializer = CarSerializer(car)
        return Response(serializer.data)


class CarSell(APIView):
    def get(self, request, pk, format=None):
        car = get_object(pk)
        if car.id_client == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        car.id_client = None
        car.save()

        serializer = CarSerializer(car)
        return Response(serializer.data)


class CarsByClient(APIView):
    def get(self, request, pkClient, format=None):
        cars = models.Car.objects.filter(id_client=pkClient)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class CarsNotSold(APIView):
    def get(self, request, format=None):
        cars = models.Car.objects.filter(id_client=None)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
