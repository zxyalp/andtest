"""
Created on 2022/3/27 0027

@author: zhou.yang
"""
from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('indexview/', views.IndexView.as_view(), name='index_view')
]
