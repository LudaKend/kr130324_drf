from celery import shared_task
from django.core.mail import send_mail
from django.core.management import settings
from config import settings
import requests
from habits.models import Habit
import datetime
from datetime import datetime, timedelta

URL = 'http:/api.telegram.org/bot'
TOKEN = settings.TELEGRAM_API_TOKEN

@shared_task
def send_habit_list():
    habit_list = Habit.objects.all(is_nice=False)  # выбираем полезные привычки
    current_date = datetime.now().date()  # текущяя дата
    for habit in habit_list:
        print(habit.data_create)
        print(habit.period)
        print(current_date - habit.data_create)


# response = requests.post(
#     url=f'{URL}{TOKEN}/отправляю напоминание', data = {'chat_id':user_telegram, 'text':text, }
# )
# print(response)
