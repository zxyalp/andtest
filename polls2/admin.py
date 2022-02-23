from django.contrib import admin

from .models import Bank, BankCard, Question, Choice

admin.site.register(Bank)
admin.site.register(BankCard)
# admin.site.register(Question)
admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
