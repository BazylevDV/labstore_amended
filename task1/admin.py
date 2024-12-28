from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, User

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # Отображаемые поля
    list_filter = ('price', 'name')  # Фильтрация по полям
    search_fields = ('name',)  # Поиск по полю
    list_per_page = 20  # Ограничение количества записей

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'password')  # Отображаемые поля
    list_filter = ('age', 'username')  # Фильтрация по полям
    search_fields = ('username',)  # Поиск по полю
    list_per_page = 30  # Ограничение количества записей
    readonly_fields = ('password',)  # Поле только для чтения