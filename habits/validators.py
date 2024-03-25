from rest_framework.serializers import ValidationError
from habits.models import Habit
from django.shortcuts import get_object_or_404


class NiceHabitValidator:
    def __init__(self, is_nice, bonus, attached_habit):
        self.field_is_nice = is_nice
        self.field_bonus = bonus
        self.attached_habit = attached_habit

    def __call__(self, value):
        #print(value)        #для отладки
        tmp_is_nice = dict(value).get(self.field_is_nice)
        #print(tmp_is_nice)    #для отладки
        tmp_bonus = dict(value).get(self.field_bonus)
        #print(tmp_bonus)    #для отладки
        tmp_attached_habit = dict(value).get(self.attached_habit)
        #print(tmp_attached_habit)    #для отладки

        # если привычка полезная
        if tmp_is_nice is False:
            if tmp_bonus is None and tmp_attached_habit is None:
                raise ValidationError('У полезной привычки нужно заполнить либо вознаграждение'
                                      ' либо связанную привычку')
            else:
                if tmp_bonus is not None and tmp_attached_habit is not None:
                    raise ValidationError('У полезной привычки можно указать либо вознаграждение,'
                                          ' либо связанную привычку')
        # иначе,т.е.привычка приятная
        else:
            if tmp_bonus is not None or tmp_attached_habit is not None:
                raise ValidationError('У приятной привычки не может быть ни вознаграждения,ни связанной привычки')


class OnlyNiceHabitValidator:
    def __init__(self, attached_habit):
        self.attached_habit = attached_habit

    def __call__(self, value):
        #print(value)  # для отладки
        tmp_attached_habit = dict(value).get(self.attached_habit)
        #print(tmp_attached_habit)  # для отладки
        if tmp_attached_habit is not None:
            # получаем запись связанной привычки из БД:
            attached_habit = get_object_or_404(Habit, id=tmp_attached_habit)
            #print(attached_habit)
            if attached_habit.is_nice is False:
                raise ValidationError('связанная привычка должна быть приятной,а не полезной')
