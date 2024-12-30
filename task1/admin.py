from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  User
from .models import Product
from .models import News


admin.site.register(Product)
admin.site.register(News)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'password')  # Отображаемые поля
    list_filter = ('age', 'username')  # Фильтрация по полям
    search_fields = ('username',)  # Поиск по полю
    list_per_page = 30  # Ограничение количества записей
    readonly_fields = ('password',)  # Поле только для чтения