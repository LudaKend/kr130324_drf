from rest_framework import generics
from habits.models import Habit
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from habits.permissions import AuthorPermissionsClass
from habits.paginators import HabitsPaginator


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """метод для записи авторизованного пользователя в качестве автора """
        #print(self.request.user)   #для отладки
        habit = serializer.save(author=self.request.user)
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated & AuthorPermissionsClass]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_queryset = queryset.filter(author=self.request.user)
        return owner_queryset


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        publish_queryset = queryset.filter(is_publish=True)
        return publish_queryset


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated & AuthorPermissionsClass]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated & AuthorPermissionsClass]
