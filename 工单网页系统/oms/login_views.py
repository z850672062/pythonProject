#!/usr/bin/env python 
# encoding: utf-8


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import *
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import reverse

def loginView(request):
    title = '用户登录'
    classContent = 'logins'
    # 处理http的post请求
    if request.method == 'POST':
        infos = LoginModelForm(data=request.POST)
        data = infos.data
        # 获取表单字段username和password的数据
        username = data['username']
        password = data['password']
        # 查找模型User是否已有用户信息
        if User.objects.filter(username=username):
            # state = '用户存在'
            # 验证用户输入的账户密码是否正确
            user = authenticate(username=username, password=password)
            # 执行登录操作
            if user:
                login(request, user)
                return redirect(reverse('oms:index'))

        else:
            # state = '无法登录'
            state = '注册成功'
            d = dict(username=username, password=password, is_staff=1, is_active=1)
            user = User.objects.create_user(**d)
            user.save()
    # 执行
    else:
        infos = LoginModelForm()
    return render(request, 'login.html', locals())


def logoutView(request):
    # 使用内置函数logout退出用户登录状态
    logout(request)
    # 网页自动跳转到登录页
    return redirect(reverse('oms:login'))

