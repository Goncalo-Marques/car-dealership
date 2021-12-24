from rest_framework import serializers
from car_dealership.models import Brand

class BrandSerializer(serializers.ModelSerializer):
     class Meta:
        model = Brand
        fields = "__all__"