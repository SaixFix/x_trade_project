from django.db import models

from trade_net.models.base import BaseModel


class SoleTrader(BaseModel):
    product = models.ForeignKey('Factory', on_delete=models.PROTECT, verbose_name='Поставщик')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальный предприниматели'