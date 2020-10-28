from django.urls import path ,include
from . import views


app_name= 'product'
urlpatterns =[
    path('',views.index , name='list'),
    path('search/', views.SearchResultsView ,name='search' ),
    path('create/' , views.create_product, name='create'),
    path('order/', views.BoughterPanel ,name='order')


    ]


