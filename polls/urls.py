# -*- coding: utf-8 -*-
"""
Created on 2020/9/7

@author: xing yan
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]
