from django.urls import path

from ..views import order_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path("add/",order_views.addOrderItems,name="add_order"),
    path("<str:pk>/",order_views.getOrder,name="get_order"),
]