from django.urls import path
from . import views


urlpatterns =[
    path('',views.index ),

    ]


#path('new' , views.new)
#path('', indexView),
#path('post/ajax/friend', postFriend, name = "post_friend"),