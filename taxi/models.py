# coding: utf-8
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    number_car = models.CharField(max_length=10)

    def __str__(self):
        return "{0} {1} {2}".format(self.pk, self.first_name, self.surname)


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    last_order = models.DateTimeField(blank=True, null=True)
    count_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{0} {1} {2}".format(self.pk, self.first_name, self.surname)


class Order(models.Model):
    """
    Тут вообщем очень спорная штука
    Я сделал отдельно поле город в котором определяем в каком городе вообще у нас заказ
    Допустим у нас система для одной страны но во многих городах
    Поле address_start (откуда едим) и address_end (куда едим), сделал TextField,
    потому что адресс состоит из многих частей(улица или переулок или квартал и т.д.)
    но как вариант, это можно было бы разбить на несколько частей, полей типа CharField
    получаем плюс в поиске по этим полям.
    """
    client = models.ForeignKey(Client)
    driver = models.ForeignKey(Driver, blank=True, null=True)
    city = models.CharField(max_length=255)
    address_start = models.TextField()
    address_end = models.TextField()
    payment = models.FloatField()
    is_close = models.BooleanField(default=False)

    def __str__(self):
        return "{0} {1} {2}".format(self.client, self.city, self.address_start)
