from car_dealership import models
from car_dealership.serializers.brand import BrandSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# view to create a new brand
class Brand(APIView):
    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view to fetch and delete a brand by Name
class BrandByName(APIView):
    def get_object(self, pk):
        try:
            return models.Brand.objects.get(pk=pk)
        except models.Brand.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view to fetch all existing brands
class Brands(APIView):
    def get(self, request, format=None):
        brands = models.Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
