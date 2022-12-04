from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=50, null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=50, null=True, blank=True)
    papa_name = models.CharField('Отчество', max_length=50, null=True, blank=True)
    iin = models.CharField('ИИН', max_length=100, null=True, blank=True)
    photo = models.ImageField('Фото', upload_to='media')
    numbers = models.CharField('Номер', max_length=14)


class Blog(models.Model):
    question = models.TextField('Вопрос')


    # like = models.DecimalField(null=True, blank=True)

class Otvet(models.Model):
    otvet = models.ForeignKey(Blog, on_delete=models.CASCADE)


class MedProduct(models.Model):
    pass

