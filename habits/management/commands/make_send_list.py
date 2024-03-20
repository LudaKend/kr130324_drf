from habits.models import Habit
import datetime
from datetime import datetime

def make_habit_list():
    habit_list = Habit.objects.filter(is_nice=False)  # выбираем полезные привычки
    current_date = datetime.now().date()  # текущяя дата
    for habit in habit_list:
        print(habit.data_create)
        print(habit.period)
        print(current_date - habit.data_create)
