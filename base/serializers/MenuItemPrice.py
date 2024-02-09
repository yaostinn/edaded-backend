from rest_framework import serializers
from base.models.MenuItem import MenuItemPrice

from base.models.Restaurateur import Restaurateur

class MenuItemPriceSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MenuItemPrice
        fields = '__all__'

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur