# Authors: Gonçalo Marques; Ricardo Vieira
# Latest change: 29/01/2022

from rest_framework import serializers
from car_dealership.models import Client
from django.contrib.auth.hashers import make_password

# client serializer based on its model
class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Client
        fields = "__all__"

    def validate(self, data):
        id = self.instance.id if self.instance != None else None

        # validating email
        email = data.get("email", None)
        if email != None:
            record = Client.objects.filter(email=email).first()
            if record != None:
                if id == None or (id != None and record.id != id):
                    raise serializers.ValidationError("Email already exists")

        # validating phone number
        phone_number = data.get("phone_number", None)
        if phone_number != None and (
            phone_number < 900000000 or phone_number > 999999999
        ):
            raise serializers.ValidationError("Invalid phone number")

        return data

    def create(self, validated_data):
        if "password" in validated_data:
            # encrypting the password
            validated_data["password"] = make_password(validated_data.get("password"))

        return super(ClientSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        instance.address = validated_data.get("address", instance.address)
        instance.phone_number = validated_data.get("phone_number", None)

        # encrypting the password
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)

        instance.save()

        return instance
