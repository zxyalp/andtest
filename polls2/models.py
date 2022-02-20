import logging

from django.db import models
from django.utils import timezone


class Bank(models.Model):
    bank_name = models.CharField(max_length=200)
    bank_code = models.IntegerField(unique=True)
    bank_abbr = models.CharField(max_length=20)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}:{}:{}'.format(self.bank_code, self.bank_name, self.bank_abbr)

    def created_days(self):
        print('now:'+str(timezone.now())+'; create_time:'+str(self.create_time))
        return (timezone.now()-self.create_time).days


class BankCard(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=20)
    card_type = models.IntegerField()
    card_length = models.IntegerField(null=True)
    card_bin = models.CharField(max_length=200)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}:{}:{}'.format(self.bank.bank_name, self.card_name, self.card_bin)
