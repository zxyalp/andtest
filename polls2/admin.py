from django.contrib import admin

from .models import Bank, BankCard, Question, Choice

admin.site.register(Bank)
admin.site.register(BankCard)
admin.site.register(Question)
admin.site.register(Choice)


