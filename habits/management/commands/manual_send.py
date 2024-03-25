from django.core.management import BaseCommand
from habits.services import make_habit_list


class Command(BaseCommand):
    def handle(self, *args, **options):
        '''формирует список отправлений'''
        make_habit_list()
