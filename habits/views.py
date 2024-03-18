from rest_framework import generics
from habits.models import Habit
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from habits.permissions import AuthorPermissionsClass
from habits.paginators import HabitsPaginator
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """метод для записи авторизованного пользователя в качестве автора """
        #print(self.request.user)   #для отладки
        habit = serializer.save(author=self.request.user)
        habit.save()

    def post(self, request):
        # print(request.data)  #для отладки
        serializer = HabitSerializer(data=request.data)
        id_attached_habit = self.request.data['attached_habit'] #получаем id связанной привычки из self.request.data
        # print(id_attached_habit)  #для отладки
        # получаем запись связанной привычки из БД:
        #attached_habit = Habit.objects.filter(id=id_attached_habit)
        attached_habit = get_object_or_404(Habit, id=id_attached_habit)
        #print(attached_habit)    #для отладки
        #print(attached_habit.is_nice)   #для отладки
        #проверяем приятная ли найденная привычка
        if attached_habit.is_nice == False:
            message = "связанная привычка должна быть приятной,а не полезной"
            return Response({"message": message})
        return Response({"message": "связанная привычка успешно присвоена"})


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

    def update(self, request, pk):
        # print(request.data)  #для отладки
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            id_attached_habit = self.request.data['attached_habit'] #получаем id связанной привычки из self.request.data
            # print(id_attached_habit)  #для отладки
            # получаем запись связанной привычки из БД:
            #attached_habit = Habit.objects.filter(id=id_attached_habit)
            attached_habit = get_object_or_404(Habit, id=id_attached_habit)
            #print(attached_habit)    #для отладки
            print(attached_habit.is_nice)   #для отладки
            #проверяем приятная ли найденная привычка
            if attached_habit.is_nice == False:
                message = "связанная привычка должна быть приятной,а не полезной"
                return Response({"message": message})
            serializer.save()
            return Response({"message": "связанная привычка успешно присвоена"})


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated & AuthorPermissionsClass]

