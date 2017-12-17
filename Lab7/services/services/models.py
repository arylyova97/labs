from django.db import models
from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CustomUser(User):
    pass


class Service(models.Model):
    title = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    company = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ('title', 'category')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    odate = models.DateField
