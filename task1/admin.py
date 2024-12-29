from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  User
from .models import Product

admin.site.register(Product)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'password')  # Отображаемые поля
    list_filter = ('age', 'username')  # Фильтрация по полям
    search_fields = ('username',)  # Поиск по полю
    list_per_page = 30  # Ограничение количества записей
    readonly_fields = ('password',)  # Поле только для чтения