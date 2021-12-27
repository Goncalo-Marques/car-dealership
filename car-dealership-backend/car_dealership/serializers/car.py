from rest_framework import serializers
from car_dealership.models import Car

# car serializer based on its model
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
