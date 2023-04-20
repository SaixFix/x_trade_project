from django.contrib import admin

from trade_net.models.factory import Factory


@admin.register(Factory)
class Factory(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'created']
    filter_horizontal = ['address', 'product']
    list_filer = ['address__city']
