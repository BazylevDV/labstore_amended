from django.urls import path
from . import views  # Импортируй представления из текущего приложения

urlpatterns = [
    path('', views.sign_up_by_html, name='sign_up_by_html'),  # Маршрут для sign_up_by_html
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),  # Маршрут для sign_up_by_django
]