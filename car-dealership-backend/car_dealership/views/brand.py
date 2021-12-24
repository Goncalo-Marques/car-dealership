from car_dealership.models import Brand
from car_dealership.serializers.brand import brandSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BrandList(APIView):
    def get(self, request, format=None):
        brands = Brand.objects.all()
        serializer = brandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = brandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetail(APIView):
    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = brandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = brandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
