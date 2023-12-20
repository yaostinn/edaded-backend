from django.contrib import admin
from base.models.Rate import Rate
from base.models.Restaurateur import Restaurateur
from base.models.Restaurant import Restaurant
from base.models.Category import Category
@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass

@admin.register(Restaurateur)
class RestaurateurAdmin(admin.ModelAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass