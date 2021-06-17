#!/usr/bin/env python 
# encoding: utf-8

from django.urls import path
from .views import *

urlpatterns = [
    #个人中心业
    path('.html', shopperView, name='shopper'),
    #登录注册页
    path('/login.html', loginView, name='login'),
    #用户注销页
    path('/logout.html', logoutView, name='logout'),
    #购物车信息页
    path('/shopcart.html', shopcartView, name='shopcart'),
    #购物车删除商品ajax
    path('/delete.html', deleteAPI, name='delete'),

]