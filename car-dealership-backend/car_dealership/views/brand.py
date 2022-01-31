# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 31/01/2022

from car_dealership import models
from car_dealership.serializers.brand import BrandSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

# returns the brand object that contains the primary key equal to 'pk' or 404 if it doesn't exist
def get_object(pk):
    try:
        return models.Brand.objects.get(pk=pk)
    except models.Brand.DoesNotExist:
        raise Http404


# view to create a new brand
class Brand(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        response = {
            "error": "Bad request: " + str(serializer.errors),
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


# view to fetch and delete a brand by Name
class BrandByName(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        brand = get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view to fetch all existing brands
class Brands(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        brands = models.Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
