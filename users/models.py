from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    telegram_id = models.CharField(max_length=90, verbose_name='telegram_id', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
