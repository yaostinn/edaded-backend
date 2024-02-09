from rest_framework import serializers
#BASE
from base.models.Category import Category
from base.models.MenuItem import MenuItem, MenuItemPrice
from base.models.Restaurant import Restaurant


class MenuItemPriceSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MenuItemPrice
        fields = '__all__'


class MenuItemSerializers(serializers.ModelSerializer):
    prices = MenuItemPriceSerializer(many=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MenuItem
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = MenuItemSerializers(many=True)

    class Meta:
        model = Category
        fields = '__all__'  

class RestaurantMenuSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    categories = CategorySerializers(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = '__all__'
