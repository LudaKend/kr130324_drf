from rest_framework.serializers import ValidationError


class NiceHabitValidator:
    def __init__(self, is_nice, bonus, attached_habit):
        self.field_is_nice = is_nice
        self.field_bonus = bonus
        self.attached_habit = attached_habit


    def __call__(self, value):
        #print(value)        #для отладки
        tmp_is_nice = dict(value).get(self.field_is_nice)
        print(tmp_is_nice)    #для отладки
        tmp_bonus = dict(value).get(self.field_bonus)
        #print(tmp_bonus)    #для отладки
        tmp_attached_habit = dict(value).get(self.attached_habit)
        #print(tmp_attached_habit)    #для отладки

        if tmp_is_nice == False:     #если привычка полезная
            if tmp_bonus == None and tmp_attached_habit == None:
                raise ValidationError(f'У полезной привычки нужно заполнить либо вознаграждение'
                                      f' либо связанную привычку')
            else:
                if tmp_bonus != None and tmp_attached_habit != None:
                    raise ValidationError(f'У полезной привычки можно указать либо вознаграждение,'
                                          f' либо связанную привычку')
        else:                        #привычка приятная
            if tmp_bonus != None or tmp_attached_habit != None:
                raise ValidationError(f'У приятной привычки не может быть ни вознаграждения,ни связанной привычки')

