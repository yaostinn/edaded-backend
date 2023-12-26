from django.urls import path
#VIEWS
from rest_framework_simplejwt.views import TokenRefreshView
#BASE VIEWS
from base.views.Token import UserTokenObtainPairView
from base.views.Restaurant import RestaurantCreateView, RestaurantUpdateOrDeleteDetailView
from base.views.Category import CategoryCreateView, CategoryUpdateOrDeleteDetailView
from base.views.MenuItem import MenuItemCreateView, MenuItemUpdateOrDeleteDetailView
from base.views.Restaurateur import RestaurateurView

from base.views.RestaurantMenu import RestaurantMenuView
urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('restaurants/', RestaurantCreateView.as_view()),
    path('restaurants/<str:pk>/', RestaurantUpdateOrDeleteDetailView.as_view()),
    
    path('category/', CategoryCreateView.as_view()),
    path('category/<str:pk>/', CategoryUpdateOrDeleteDetailView.as_view()),

    path('menu-item/', MenuItemCreateView.as_view()),
    path('menu-item/<str:pk>/', MenuItemUpdateOrDeleteDetailView.as_view()),

    path('restaurateur/', RestaurateurView.as_view()),
    path('restaurant-menu/<uuid:pk>/', RestaurantMenuView.as_view()),
]