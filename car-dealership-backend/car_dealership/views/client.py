from operator import truediv
from car_dealership import models
from car_dealership.serializers.client import ClientSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# returns the client object that contains the primary key equal to 'pk' or 404 if it doesn't exist
def get_object(pk):
    try:
        return models.Client.objects.get(pk=pk)
    except models.Client.DoesNotExist:
        raise Http404


# checks if the client has any invalid fields
def is_valid(object):
    if object["phone_number"] < 900000000 or object["phone_number"] > 999999999:
        return False
    return True


# view to create a new client
class Client(APIView):
    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            if not is_valid(serializer.validated_data):
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to fetch, update and delete a client by ID
class ClientByID(APIView):
    def get(self, request, pk, format=None):
        client = get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            if not is_valid(serializer.validated_data):
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view to fetch all existing clients
class Clients(APIView):
    def get(self, request, format=None):
        clients = models.Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
