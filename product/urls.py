from django.urls import path ,include
from . import views



urlpatterns =[
    path('',views.index ),
    path('search/', views.SearchResultsView.as_view() ),
    path('order/', views.BoughterPanel ,name='order')


    ]


