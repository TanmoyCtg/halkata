from django.conf.urls import url 
from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home,name='home'),
    path('singlepost/<id>', views.single_post,name='single_post'),
    path('posts/', views.all_posts, name='all_posts'),
    
]
