from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

#BASE
from base.serializers.MenuItem import MenuItemSerializers
from base.models.MenuItem import MenuItem
from base.permissions.MenuItem import CanCreateMenuItem, CanUpdateOrDeleteMenuItem


class MenuItemCreateView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializers
    permission_classes = [
        IsAuthenticated,
        CanCreateMenuItem,
    ]

    def get_queryset(self):
        return MenuItem.objects.filter(owner__user=self.request.user)
    
class MenuItemUpdateOrDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializers
    permission_classes = [
        IsAuthenticated,
        CanUpdateOrDeleteMenuItem
        ]
    
    def get_queryset(self):
        return MenuItem.objects.filter(owner__user=self.request.user)