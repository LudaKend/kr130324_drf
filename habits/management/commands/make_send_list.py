from habits.models import Habit
import datetime
from datetime import datetime
from django.shortcuts import get_object_or_404
from users.models import User
import requests
from config import settings

def make_habit_list():
    habit_list = Habit.objects.filter(is_nice=False)  # выбираем полезные привычки
    current_date = datetime.now().date()  # текущяя дата
    send_list = []
    for habit in habit_list:
        #print(habit.data_create)   #для отладки
        #print(habit.period)        #для отладки
        delta = current_date - habit.data_create
        #print(delta.days)          #для отладки
        if delta.days % habit.period == 0:
            send_list.append(habit)
    print(send_list)

    # URL = 'https://api.telegram.org/bot'
    # TOKEN = settings.TELEGRAM_API_TOKEN
    # for send in send_list:
    #     print(send.author)
    #     tmp_user = get_object_or_404(User, email=send.author)
    #     print(tmp_user.telegram)
    #     text = f'{send.habit} в {send.habit_time} в {send.place}'
    #     response = requests.post(url=f'{URL}{TOKEN}/sendMessage',
    #                              data={'chat_id': tmp_user.telegram, 'text': text, })
    #
    #     print(response.status_code)    #для отладки
    #     print(response.json())         #для отладки

    return send_list
