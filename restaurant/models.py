from cgi import print_exception
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=18)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
