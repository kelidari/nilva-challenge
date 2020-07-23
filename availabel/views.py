from django.http.response import JsonResponse
from rest_framework.views import  APIView
from product.models import Product
from .serializers import  ProductSerializer




class ProductList(APIView):
    queryset = Product.objects.all()
    def get(self,request):
        Shoes =Product.objects.all()
        serializer = ProductSerializer(Shoes , many=True)
        return JsonResponse(serializer.data,safe=False)

