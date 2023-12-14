from django.db import models
from base.models.Restaurateur import Restaurateur


class Base(models.Model):
    owner = models.ForeignKey('base.Restaurateur', on_delete=models.CASCADE, verbose_name='Ресторатор')