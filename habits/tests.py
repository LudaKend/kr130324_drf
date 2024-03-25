from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from habits.models import Habit
from django.urls import reverse


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='autotest@mail.ru', password='init_init', telegram='1168927684')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(habit='приятная привычка для теста', author=self.user,
                                          place='в приятном для теста месте', habit_time="07:07:07",
                                          lead_time_new="77", is_nice=True, period='1')

    def test_get_list(self):
        self.data = {'habit': self.habit.id}
        response = self.client.get('/habits/list_view/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Habit.objects.filter(id=self.habit.id).exists())

    def test_get_publish_list(self):
        self.data = {'habit': 'полезная привычка для теста', 'author': self.user.id,
                     'place': 'в полезном для теста месте', 'habit_time': '08:08:08',
                     'lead_time_new': '88', 'is_nice': 'False', 'period': '2', 'bonus': 'еще один тест',
                     'is_publish': 'True'}
        response = self.client.get('/habits/public_view/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Habit.objects.filter(id=self.habit.id).exists())
        self.data = {'habit': 'полезная привычка для теста', 'author': self.user.id,
                     'place': 'в полезном для теста месте', 'habit_time': '08:08:08',
                     'lead_time_new': '88', 'is_nice': 'False', 'period': '2', 'bonus': 'еще один тест',
                     'is_publish': 'False'}
        response = self.client.get('/habits/public_view/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        self.data = {'habit': 'полезная привычка для теста', 'author': self.user.id,
                     'place': 'в полезном для теста месте', 'habit_time': '08:08:08',
                     'lead_time_new': '88', 'is_nice': 'False', 'period': '2', 'bonus': 'еще один тест'}
        self.url = reverse('habits:habit_create')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.filter(habit='полезная привычка для теста').exists())

    def test_update(self):
        self.data = {'habit': 'измененная привычка для теста', 'author': self.user.id,
                     'place': 'в измененном для теста месте', 'habit_time': '09:09:09',
                     'lead_time_new': '99', 'is_nice': 'False', 'period': '2', 'bonus': 'еще один тест',
                     'is_publish': 'True'}
        self.url = reverse('habits:habit_update', kwargs={'pk': self.habit.id})
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Habit.objects.filter(is_publish='True').exists())

    def test_delete(self):
        self.url = reverse('habits:habit_delete', kwargs={'pk': self.habit.id})
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())
