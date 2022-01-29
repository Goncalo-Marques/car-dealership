from car_dealership import models
from car_dealership.serializers.client import ClientSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

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

    def get(self, request, pk, format=None):
        client = get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

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
            return Response(serializer.data)

        response = {
            "error": "Bad request: " + str(serializer.errors),
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view to fetch all existing clients
class Clients(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        clients = models.Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
