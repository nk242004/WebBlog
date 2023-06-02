from rest_framework import serializers
from sportsman.models import *


class SportsmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportsman
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'