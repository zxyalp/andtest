from django.contrib import admin

# Register your models here.
from .models import Question, Choice


admin.register()

admin.site.register(Question)
admin.site.register(Choice)
