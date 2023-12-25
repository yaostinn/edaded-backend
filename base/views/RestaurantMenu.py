#REST
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from base.serializers.RestaurantMenu import RestaurantMenuSerializers
from base.models.Restaurant import Restaurant
class RestaurantMenuView(generics.ListAPIView):
    serializer_class = RestaurantMenuSerializers
    permission_classes = [IsAuthenticated, ]
    pagination_class = None
    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)
  