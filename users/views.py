from rest_framework import generics, status
from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """метод для записи хэш-пароля """
        user = serializer.save()
        password = serializer.data["password"]
        user.set_password(password)
        user.save()

    def create(self, request, *args, **kwargs):
        """метод для сохранения хешированного пароля в бд (если пароль
         не хешируется - пользователь не считается активным и токен
         авторизации не создается)"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
