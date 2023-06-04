import datetime

from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    about = models.CharField(max_length=150, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='превью')
    category = models.CharField(max_length=150, verbose_name='категория')
    price_lot = models.IntegerField(verbose_name='цена за покупку')
    date_create = models.DateTimeField(verbose_name='дата создания')
    date_last_change = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}: {self.about}'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    about = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.name}: {self.about}'

