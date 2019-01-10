from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.my_expense, name='cost_list'),
]
