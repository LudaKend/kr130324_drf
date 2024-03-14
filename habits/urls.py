from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitUpdateAPIView, HabitListAPIView, HabitPublicListAPIView,\
    HabitDestroyAPIView
from django.urls import path

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('list_view/', HabitListAPIView.as_view(), name='habit_list'),
    path('public_view/', HabitPublicListAPIView.as_view(), name='habit_public'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    ]
