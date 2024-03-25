from rest_framework import serializers
from habits.models import Habit
from habits.validators import NiceHabitValidator, OnlyNiceHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [NiceHabitValidator('is_nice', 'bonus', 'attached_habit'),
                      OnlyNiceHabitValidator('attached_habit')]
