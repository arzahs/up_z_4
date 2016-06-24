# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    passport = models.CharField(max_length=6)
    city = models.CharField(max_length=255)
    years_old = models.PositiveIntegerField()

    def __str__(self):
        return '{0}-{1} {2}'.format(self.passport, self.first_name, self.surname)


class ClientEmail(models.Model):
    client = models.ForeignKey(Client)
    email = models.EmailField()


class ClientPhone(models.Model):
    client = models.ForeignKey(Client)
    number = models.CharField(max_length=12)


class Tour(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    price = models.FloatField()
    number_seats = models.PositiveIntegerField()
    number_people = models.PositiveIntegerField()
    data_start = models.DateTimeField()
    data_end = models.DateTimeField()
    is_close = models.BooleanField(default=False)

    def __str__(self):
        return "{0} ({1}-{2}) price:{3}".format(self.city, self.data_start.date(), self.data_end.date(), self.price)


class Payment(models.Model):
    payment_choices = (
        (1, "Забронирован"),
        (2, "Частично оплачен"),
        (3, "Оплачен")
    )

    client = models.ForeignKey(Client)
    tour = models.ForeignKey(Tour)
    payment_summ = models.FloatField(blank=True, null=True)
    payment_status = models.PositiveIntegerField(choices=payment_choices)

    def __str__(self):
        return "{0} {1} {2}".format(self.client, self.tour, self.payment_status)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = u"Payments"
