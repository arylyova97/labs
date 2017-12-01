from django.contrib import admin

from .models import CustomUser, Service, Order

admin.site.register(CustomUser)
admin.site.register(Service)
admin.site.register(Order)
