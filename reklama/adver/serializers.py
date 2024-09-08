from rest_framework import serializers
from .models import Adver, Street, Region, Adver_type


class AdverSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    image_url = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

    class Meta:
        model = Adver
        fields = ['title', 'content', 'address', 'contact', 'street', 'type', 'user', 'status', 'price', 'price_type',
                  'created_at', 'image', 'image_url']


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class Adver_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adver_type
        fields = '__all__'
