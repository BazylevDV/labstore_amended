from django.db import models



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
