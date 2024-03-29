"""
Created on 2022/3/27 0027 11:44

@author: zhou.yang
"""
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字!')
        return int(cleaned_data)

    class Meta:
        model = Student

        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )

