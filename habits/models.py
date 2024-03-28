from django.db import models
from config import settings
from django.core.validators import MaxValueValidator

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    place = models.CharField(max_length=100, verbose_name='Место')
    habit_time = models.TimeField(verbose_name='Время', default='09:00:00')
    habit = models.CharField(max_length=500, verbose_name='Привычка')
    is_nice = models.BooleanField(verbose_name='Приятная привычка',
                                  default=False)
    attached_habit_new = models.ForeignKey('Habit',
                                           verbose_name='Связанная привычка',
                                           **NULLABLE,
                                           on_delete=models.SET_NULL,
                                           related_name='nice_habit')
    period = models.IntegerField(verbose_name='Периодичность в днях',
                                 validators=[MaxValueValidator(7)],
                                 default='1')
    bonus = models.CharField(max_length=500, verbose_name='Вознаграждение',
                             **NULLABLE)
    lead_time_new = models.IntegerField(verbose_name='Время на  выполнение'
                                                     ' привычки в секундах',
                                        validators=[MaxValueValidator(120)],
                                        default='1')  # не больше 120секунд!
    is_publish = models.BooleanField(verbose_name='Общий доступ',
                                     default=False)
    data_create = models.DateField(verbose_name='дата создания',
                                   auto_now_add=True)

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.id}, {self.author}, {self.habit},' \
               f' {self.habit_time}, {self.place}, {self.is_nice}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
