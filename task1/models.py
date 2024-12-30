from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Поле description
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)  # Заголовок новости
    content = models.TextField()  # Содержание новости
    date = models.DateTimeField(default=timezone.now)  # Дата новости

    def __str__(self):
        return self.title