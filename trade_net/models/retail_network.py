from django.db import models

from trade_net.models.base import BaseModel


class RetailNetwork(BaseModel):
    product = models.ForeignKey('Factory', on_delete=models.PROTECT, verbose_name='Поставщик')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничная сети'
