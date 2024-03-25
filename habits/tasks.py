from celery import shared_task
from config import settings
import requests
from users.models import User
from habits.services import make_habit_list
from django.shortcuts import get_object_or_404


URL = 'https://api.telegram.org/bot'
TOKEN = settings.TELEGRAM_API_TOKEN


@shared_task
def send_habit_list():
    send_list = make_habit_list()
    for send in send_list:
        tmp_user = get_object_or_404(User, email=send.author)
        #print(tmp_user.telegram)       #для отладки
        text = f'{send.habit} в {send.habit_time} в {send.place}'
        #print(text)                    #для отладки
        response = requests.post(url=f'{URL}{TOKEN}/sendMessage',
                                 data={'chat_id': tmp_user.telegram, 'text': text, })

        print(response.status_code)
        #print(response.json())         #для отладки
