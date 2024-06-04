from django.db import models

from config import settings


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    place = models.CharField(max_length=100, verbose_name='место выполнения привычки')
    time = models.TimeField(verbose_name='время исполнения')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    related_habit = models.ForeignKey(
        'Habit',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='связанная привычка'
    )
    periodicity = models.SmallIntegerField(default=1, verbose_name='периодичность выполнения в днях')
    reward = models.CharField(max_length=100, null=True, blank=True, verbose_name='награда')
    expected_completion_time = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='признак публичности')

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
