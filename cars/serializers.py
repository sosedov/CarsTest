from rest_framework import serializers
from .models import CarsLabel

class CarsLabelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    country = serializers.CharField()
    id = serializers.IntegerField()
    def create(self, validated_data):
        return CarsLabel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.title)
        instance.country = validated_data.get('country', instance.description)        
        instance.id = validated_data.get('id', instance.author_id)
        instance.save()
        return instance