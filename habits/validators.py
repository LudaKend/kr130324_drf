from rest_framework.serializers import ValidationError


class UsefulHabitValidator:
    def __init__(self, is_nice, bonus, attached_habit_new):
        self.field_is_nice = is_nice
        self.field_bonus = bonus
        self.attached_habit_new = attached_habit_new

    def __call__(self, value):
        tmp_is_nice = dict(value).get(self.field_is_nice)
        tmp_bonus = dict(value).get(self.field_bonus)
        tmp_attached_habit_new = dict(value).get(self.attached_habit_new)
        # если привычка полезная
        if tmp_is_nice is False:
            if tmp_bonus is None and tmp_attached_habit_new is None:
                raise ValidationError('У полезной привычки нужно '
                                      'заполнить либо вознаграждение'
                                      ' либо связанную привычку')
            else:
                if tmp_bonus is not None and \
                        tmp_attached_habit_new is not None:
                    raise ValidationError('У полезной привычки можно указать '
                                          'либо вознаграждение,'
                                          ' либо связанную привычку')


class NiceHabitValidator:
    def __init__(self, is_nice, bonus, attached_habit_new):
        self.field_is_nice = is_nice
        self.field_bonus = bonus
        self.attached_habit_new = attached_habit_new

    def __call__(self, value):
        tmp_is_nice = dict(value).get(self.field_is_nice)
        tmp_bonus = dict(value).get(self.field_bonus)
        tmp_attached_habit_new = dict(value).get(self.attached_habit_new)
        if tmp_is_nice is True:
            if tmp_bonus is not None or tmp_attached_habit_new is not None:
                raise ValidationError('У приятной привычки не может быть'
                                      ' ни вознаграждения,'
                                      'ни связанной привычки')


class OnlyNiceHabitValidator:
    def __init__(self, attached_habit_new):
        self.attached_habit_new = attached_habit_new

    def __call__(self, value):
        print(value)  # для отладки
        tmp_attached_habit_new = dict(value).get(self.attached_habit_new)
        print(tmp_attached_habit_new)  # для отладки

        if tmp_attached_habit_new is not None:
            if tmp_attached_habit_new.is_nice is False:
                raise ValidationError('связанная привычка '
                                      'должна быть приятной,а не полезной')
