from habits.models import Habit
from datetime import datetime


def make_habit_list():
    habit_list = Habit.objects.filter(is_nice=False)
    current_date = datetime.now().date()  # текущяя дата
    send_list = []
    for habit in habit_list:
        delta = current_date - habit.data_create
        if delta.days % habit.period == 0:
            send_list.append(habit)
    return send_list
