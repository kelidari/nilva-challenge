from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    explain = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)


class Bought (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    boughter = models.ForeignKey(User, on_delete=models.CASCADE)


