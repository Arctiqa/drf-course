from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.test',
            password='test',
            telegram_id='123'
        )

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='test_place',
            time='14:00:00',
            action='test_action',
            periodicity=5,
            reward='test_reward',
            expected_completion_time=70,
            is_public=True
        )

    def test_create_habit(self):
        data = {
            'user': self.user.id,
            'place': 'test_place',
            'time': '14:00:00',
            'action': 'test_action',
            'periodicity': 5,
            'reward': 'test_reward',
            'expected_completion_time': 70,
            'is_public': True
        }
        response = self.client.post('/habits/create/', data=data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_habit(self):
        response = self.client.get(f'/habits/{self.habit.pk}/detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        data = {
            'time': '12:00:00',
            'action': 'test_action_1',
            'expected_completion_time': 60,
            'periodicity': 5
        }
        response = self.client.patch(f'/habits/{self.habit.pk}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['time'], '12:00:00')

    def test_habit_list(self):
        response = self.client.get('/habits/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        response = self.client.delete(f'/habits/{self.habit.pk}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
