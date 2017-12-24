from django.db import models
from django import forms
from datetime import date, datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image

# Create your models here.
from django.template.backends import django


class CustomUser(User):
    pass


class ServiceManager(models.Manager):
    def get_services(self, limit, offset):
        return self.all()[offset:limit + offset]


class Service(models.Model):
    title = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    company = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_info = models.TextField(default="")
    top = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/img')
    objects = ServiceManager()

    def __str__(self):
        return self.company + ': ' + self.title

    class Meta:
        unique_together = ('title', 'company')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    odate = models.DateField(default=datetime.now())


