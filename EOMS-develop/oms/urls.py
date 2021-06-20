#!/usr/bin/env python 
# encoding: utf-8
from django.urls import path
from .login_views import *
from .views import *

urlpatterns = [
    # 个人中心业
    path('/index.html', index, name='index'),
    #登录注册页
    path('', loginView, name='login'),
    #用户注销页
    path('/logout.html', logoutView, name='logout'),


]