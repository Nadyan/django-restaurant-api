from rest_framework import generics

from restaurant.models import Dish
from restaurant.serializers import DishSerializer

# Django view is the controller

class DishListView(generics.ListAPIView):
    # ListAPIView: List items
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
