from users.apps import UsersConfig
from users.views import UserCreateAPIView, MyTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register/', UserCreateAPIView.as_view(), name='register_users'),
]
