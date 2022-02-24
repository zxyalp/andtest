from django.contrib import admin

from .models import Bank, BankCard, Question, Choice

admin.site.register(Bank)
admin.site.register(BankCard)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Context', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
