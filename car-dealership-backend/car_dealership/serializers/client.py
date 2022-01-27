from rest_framework import serializers
from car_dealership.models import Client

# client serializer based on its model
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        # validating phone number
        if data["phone_number"] < 900000000 or data["phone_number"] > 999999999:
            raise serializers.ValidationError("Invalid phone number")
        return data

    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
    # TODO: encriptar password
