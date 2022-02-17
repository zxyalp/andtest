from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=200)
    bank_code = models.IntegerField()
    bank_abbr = models.CharField(max_length=20)


class BankCard(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    card_type = models.IntegerField()
    card_name = models.CharField(max_length=20)
    card_bin = models.CharField(max_length=200)
