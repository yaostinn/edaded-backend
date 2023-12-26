from django.db import models
from base.models.Base import Base
from base.models.Category import Category


class MenuItem(Base):
    name = models.CharField(max_length=255)
    category_ref = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'items')

    def __str__(self):
        return self.name