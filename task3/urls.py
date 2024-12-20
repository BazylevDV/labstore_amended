from django.urls import path
from . import views

urlpatterns = [
    path('', views.labtorg, name='labtorg'),
    path('reagents/', views.reagents, name='reagents'),
    path('basket/', views.basket, name='basket'),
]