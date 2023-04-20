from django.contrib import admin

from trade_net.models.base import Product, Address
from trade_net.models.factory import Factory


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ['country', 'city', 'street', 'house_number']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['title', 'model', 'release_date']
    ordering = ['-release_date', 'title']


@admin.action(description='Очистить задолжность')
def make_zero(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Factory)
class Factory(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'created', 'address']
    filter_horizontal = ['product']
    ordering = ['address__city']
    actions = [make_zero]
