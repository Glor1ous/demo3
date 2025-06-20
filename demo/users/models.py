from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    Класс пользователя (здесь указываются все ваши поля)
    """
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
