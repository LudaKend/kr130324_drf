from django.db import models
from config import settings
from django.core.validators import MaxValueValidator

NULLABLE = {'null': True, 'blank': True}

class Habit(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='Автор')
    place = models.CharField(max_length=100, verbose_name='Место')
    habit_time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=500, verbose_name='Привычка')
    is_nice = models.BooleanField(verbose_name='Приятная привычка', default=False)
    attached_habit = models.IntegerField(verbose_name='Привязанная привычка', **NULLABLE)
    period = models.IntegerField(verbose_name='Периодичность в днях', **NULLABLE, validators=[MaxValueValidator(7)])
                                                                                                        #не больше 7!
    bonus = models.CharField(max_length=500, verbose_name='Вознаграждение')
    lead_time = models.TimeField(verbose_name='Время на  выполнение привычки')  #, max_value='00:02:00')
                                                                                #не больше 120секунд!
    is_publish = models.BooleanField(verbose_name='Общий доступ', default=False)

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.author}, {self.action}, {self.habit_time}, {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
