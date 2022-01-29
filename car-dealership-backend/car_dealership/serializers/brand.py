# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 27/12/2021

from rest_framework import serializers
from car_dealership.models import Brand

# brand serializer based on its model
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
