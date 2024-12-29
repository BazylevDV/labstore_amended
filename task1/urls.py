from django.urls import path
from . import views  # Импортируем представления из текущего приложения

urlpatterns = [
    path('labtorg/', views.labtorg, name='labtorg'),  # Маршрут для страницы labtorg
    path('reagents/', views.reagents, name='reagents'),  # Маршрут для страницы reagents
    path('buy/<int:product_id>/', views.buy, name='buy'),
    path('basket/', views.basket, name='basket'),  # Маршрут для страницы basket
    path('sign_up_by_django/', views.sign_up_by_django, name='sign_up_by_django'),  # Маршрут для регистрации через Django
    path('sign_up_by_html/', views.sign_up_by_html, name='sign_up_by_html'),  # Маршрут для регистрации через HTML

]
