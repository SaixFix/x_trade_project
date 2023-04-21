from django.db import models

from trade_net.models.base import BaseModel


class SoleTrader(BaseModel):
    provider = models.ForeignKey('Factory', on_delete=models.SET_NULL, verbose_name='Поставщик', null=True)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'