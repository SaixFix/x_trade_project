from django.contrib import admin

from trade_net.models import base
from trade_net.models.factory import Factory
from trade_net.models.retail_network import RetailNetwork
from trade_net.models.sole_trader import SoleTrader


@admin.register(base.Address)
class Address(admin.ModelAdmin):
    list_display = ['country', 'city', 'street', 'house_number']


@admin.register(base.Product)
class Product(admin.ModelAdmin):
    list_display = ['title', 'model', 'release_date']
    ordering = ['-release_date', 'title']


@admin.action(description='Очистить задолжность')
def make_zero(modeladmin, request, queryset):
    """Добовляет в админку экшн обнуляющий задолжность"""
    queryset.update(debt=0)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'address']
    list_display_links = ('title',)
    filter_horizontal = ['product']
    actions = [make_zero]

    def address(self, obj):
        """Функция сортировки страки адресс по городу"""
        return obj.addres.city

    address.admin_order_field = 'address__city'


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'address']
    list_display_links = ('title',)
    filter_horizontal = ['product']
    actions = [make_zero]

    def address(self, obj):
        """Функция сортировки страки адресс по городу"""
        return obj.addres.city

    address.admin_order_field = 'address__city'


@admin.register(SoleTrader)
class SoleTraderAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'address']
    list_display_links = ('title',)
    filter_horizontal = ['product']
    actions = [make_zero]

    def address(self, obj):
        """Функция сортировки страки адресс по городу"""
        return obj.addres.city

    address.admin_order_field = 'address__city'
