from django.urls import path
from ..views import user_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('', user_views.getUsers, name="get_users"),
    path('update/profile/', user_views.updateUserProfile, name="update_user"),
    path('register/', user_views.registerUser, name="register_user"),
    path('profile/', user_views.getUserProfile, name='user_profile'),
    path('login/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]