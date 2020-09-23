from django.urls import path ,include
from . import views


urlpatterns =[
    path('ProductList/',views.ProductList.as_view() ),
   # path('ProductList/<int:Product_id>/',views.FilterProductList.as_view() ),
     path('UserList/',views.UserList.as_view() ),

    ]

