from rest_framework import serializers
from car_dealership.models import Client

# client serializer based on its model
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
