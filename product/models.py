from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    explain = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)

