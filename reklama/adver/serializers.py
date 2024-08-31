from rest_framework import serializers
from .models import Adver


class AdverSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    image_url = serializers.CharField(required=False)
    status = serializers.CharField(required=False)


    class Meta:
        model = Adver
        fields = ['title', 'content', 'address', 'contact', 'street', 'type', 'user', 'status', 'price',
                  'created_at', 'image', 'image_url']
