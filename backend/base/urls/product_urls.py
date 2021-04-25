from django.urls import path
from ..views import product_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('',product_views.getProducts,name='products'),
    path('<str:pk>/',product_views.getProduct, name='product')
]