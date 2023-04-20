from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from trade_net.models import base
from trade_net.models.factory import Factory


@admin.register(base.Address)
class Address(admin.ModelAdmin):
    list_display = ['country', 'city', 'street', 'house_number']


@admin.register(base.Product)
class Product(admin.ModelAdmin):
    list_display = ['title', 'model', 'release_date']
    ordering = ['-release_date', 'title']


@admin.action(description='Очистить задолжность')
def make_zero(modeladmin, request, queryset):
    queryset.update(debt=0)


class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'created', 'address']
    list_display_links = ('title',)
    filter_horizontal = ['product']
    actions = [make_zero]

    def address(self, obj):
        return obj.author.first_name

    address.admin_order_field = 'address__city'


admin.site.register(Factory, FactoryAdmin)
