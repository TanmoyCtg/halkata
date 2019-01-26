from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.my_expense, name='costlist'),
    path('add/', views.add_expense, name='addexpense'),
]
