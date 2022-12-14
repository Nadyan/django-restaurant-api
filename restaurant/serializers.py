from pyexpat import model
from rest_framework import serializers
from restaurant.models import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
