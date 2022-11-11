from rest_framework import serializers
from .models import Item, Image


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
