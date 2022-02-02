# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 02/02/2022

from car_dealership import models
from car_dealership.serializers.client import ClientSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# returns the client object that contains the primary key equal to 'pk' or 404 if it doesn't exist
def get_object(pk):
    try:
        return models.Client.objects.get(pk=pk)
    except models.Client.DoesNotExist:
        raise Http404


# view to fetch, update and delete a client by ID
class ClientByID(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Gets a client by id",
        responses={
            "200": openapi.Response(
                description="OK",
                schema=ClientSerializer(),
            ),
            "404": "Not found",
        },
    )
    def get(self, request, pk, format=None):
        client = get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Updates a client by id",
        request_body=ClientSerializer(),
        responses={
            "200": openapi.Response(
                description="OK",
                schema=ClientSerializer(),
            ),
            "400": "Bad request",
            "403": "Forbidden",
            "404": "Not found",
        },
    )
    def put(self, request, pk, format=None):
        # validate user authority
        if request.user.id != pk:
            response = {
                "error": "Forbidden: user cannot take actions for other users",
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        client = get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # updates the client login if password changed
            password = request.data.get("password", None)
            if password != None:
                auth = authenticate(
                    request, email=serializer.data.get("email", None), password=password
                )
                login(request, auth)

            return Response(serializer.data)

        response = {
            "error": "Bad request: " + str(serializer.errors),
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Deletes a client by id",
        responses={
            "204": "No content",
            "404": "Not found",
        },
    )
    def delete(self, request, pk, format=None):
        client = get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view to fetch all existing clients
class Clients(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get all clients",
        responses={
            "200": openapi.Response(
                description="OK",
                schema=ClientSerializer(many=True),
            ),
        },
    )
    def get(self, request, format=None):
        clients = models.Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
