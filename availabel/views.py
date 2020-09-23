from django.http.response import JsonResponse
from rest_framework.views import  APIView
from product.models import Product
from django.contrib.auth.models import User
from .serializers import  ProductSerializer,UserSerializer


class UserList(APIView):
    queryset = User.objects.all()
    def get(self,request):
        persons =User.objects.all()
        serializer = UserSerializer(persons , many=True)
        return JsonResponse(serializer.data,safe=False)



class ProductList(APIView):
    queryset = Product.objects.all()
    def get(self,request):
        Shoes =Product.objects.all()
        serializer = ProductSerializer(Shoes , many=True)
        return JsonResponse(serializer.data,safe=False)


# class FilterProductList(APIView):
#     def get(self,request, **kwargs):
#       queryset = Product.objects.filter.get(id=kwargs['Product_id'])
#       serializer = ProductSerializer(queryset , many=True)
#       return JsonResponse(serializer.data,safe=False)




