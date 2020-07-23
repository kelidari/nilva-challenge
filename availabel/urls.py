from django.urls import path ,include
from . import views


urlpatterns =[
    path('',views.ProductList.as_view() ),

    ]

