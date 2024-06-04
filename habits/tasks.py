from datetime import datetime, timedelta

import requests
from celery import shared_task

from config.settings import TELEGRAM_TOKEN
from habits.models import Habit
from users.models import User


@shared_task
def send_notification():
    """Уведомление о выполнении привычки"""
    current_time = datetime.now().replace(second=0, microsecond=0)

    habits = Habit.objects.filter(time=current_time)
    print(habits)

    for habit in habits:
        if habit.time == current_time.time() or habit.time == current_time:

            reward = ''
            if habit.reward:
                reward = f'Награда: {habit.reward}'
            elif habit.related_habit:
                reward = f'Награда: {habit.related_habit.action}'

            message = (f"Время закрепить привычку:"
                       f"\nДействие: {habit.action}\nМесто: {habit.place}\n{reward}")

            user = User.objects.get(pk=habit.user.pk)
            if user.telegram_id:
                requests.post(
                    f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage',
                    params={
                        'chat_id': user.telegram_id,
                        'text': message,
                    }
                )
            next_date = datetime.now().replace(second=0, microsecond=0) + timedelta(days=habit.periodicity)

            habit.time = next_date
            habit.save()
