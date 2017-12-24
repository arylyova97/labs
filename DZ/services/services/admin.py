from django.contrib import admin

from .models import CustomUser, Service, Order

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'company', 'price', 'short_info','top')
    list_filter = ('company', 'title')
    search_fields = ('company', 'title')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'service')
    list_filter = ('user', 'service')
    search_fields = ('user', 'service')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
