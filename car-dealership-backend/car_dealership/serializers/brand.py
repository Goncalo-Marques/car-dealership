from rest_framework import serializers
from car_dealership.models import Brand

class brandSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    
    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        
        instance.save()
        return instance

