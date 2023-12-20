from django.db import models
from base.models.Base import Base


class MenuItem(Base):
    name = models.CharField(max_length=255)
    category_ref = models.ForeignKey('base.Category', on_delete=models.CASCADE)