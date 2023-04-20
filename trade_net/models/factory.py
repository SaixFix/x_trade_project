from django.db import models

from trade_net.models.base import BaseModel


class Factory(BaseModel):

    class Meta:
        verbose_name = 'Фабрика'
        verbose_name_plural = 'Фабрики'
