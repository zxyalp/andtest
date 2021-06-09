# -*- coding: utf-8 -*-
"""
Created on 2021/6/1

@author: yang.zhou
"""
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index')
]
