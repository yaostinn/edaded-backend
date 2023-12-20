from django.db import models

from base.models.Base import Base

class Category(Base):
    restaurant_ref = models.ForeignKey('base.Restaurant', on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)