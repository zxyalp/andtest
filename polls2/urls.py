"""
Created on 2022/2/17 0017

@author: zhou.yang
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]