from django.urls import path
#VIEWS
from rest_framework_simplejwt.views import TokenRefreshView
#BASE VIEWS
from base.views.Token import UserTokenObtainPairView
from base.views.Restaurant import RestaurantCreateView, RestaurantUpdateOrDeleteDetailView

urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('restaurant/', RestaurantCreateView.as_view(), name = 'restaurant urls'),
    path('restaurant/<int:pk>/', RestaurantUpdateOrDeleteDetailView.as_view()),
]