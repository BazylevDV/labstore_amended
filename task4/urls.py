from django.urls import path
from . import views

urlpatterns = [
    path('', views.labtorg, name='labtorg'),  # Главная страница (пустой путь)
    path('reagents/', views.reagents, name='reagents'),  # Страница реагентов
    path('basket/', views.basket, name='basket'),  # Страница корзины
]