from rest_framework import serializers
from base.models.MenuItem import MenuItem

from base.models.Restaurateur import Restaurateur

class MenuItemSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MenuItem
        fields = '__all__'

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur