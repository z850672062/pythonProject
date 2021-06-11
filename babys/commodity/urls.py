#!/usr/bin/env python 
# encoding: utf-8
from django.urls import path
from .views import *

urlpatterns = [
    #定义商品列表页
    path('.html', commodityView, name='commdityView'),
    #定义商品详细页
    #<int:id>为变量，他以整数型表示，变量id对应商品信息表的主键id，改变变量id的数值可以查看不同商品的详细介绍
    #路由地址末端设置.html 是一种伪静态技术，此外还可以为变量id设置终止符。不然随便输入无限长的数字也能正常访问
    path('/detail.<int:id>.html', detailView, name='detail'),



]