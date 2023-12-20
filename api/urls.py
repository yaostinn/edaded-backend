from django.urls import path
#VIEWS
from rest_framework_simplejwt.views import TokenRefreshView
#BASE VIEWS
from base.views.Token import UserTokenObtainPairView
from base.views.Restaurant import RestaurantCreateView, RestaurantUpdateOrDeleteDetailView
from base.views.Category import CategoryCreateView, CategoryUpdateOrDeleteDetailView
from base.views.MenuItem import MenuItemCreateView, MenuItemUpdateOrDeleteDetailView
urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('restaurant/', RestaurantCreateView.as_view()),
    path('restaurant/<int:pk>/', RestaurantUpdateOrDeleteDetailView.as_view()),
    
    path('category/', CategoryCreateView.as_view()),
    path('category/<int:pk>/', CategoryUpdateOrDeleteDetailView.as_view()),

    path('menu-item/', MenuItemCreateView.as_view()),
    path('menu-item/<int:pk>/', MenuItemUpdateOrDeleteDetailView.as_view()),
]