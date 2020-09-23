from rest_framework import serializers
from product.models import  Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('name','price','explain','image_url')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email')