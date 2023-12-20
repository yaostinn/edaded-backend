from django.db import models
from base.models.Base import Base


class Restaurant(Base):
    name = models.CharField(max_length=100)
    image = models.ImageField('Картика',upload_to='restaurants/', blank=True, null=True)
    address = models.CharField('Адрес', max_length=100, blank=True, null=True)
    is_visible = models.BooleanField('Видимость', default=True)

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):      
        return self.name