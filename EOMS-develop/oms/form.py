#!/usr/bin/env python 
# encoding: utf-8

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=11, label='请您输入手机号',
#                                widget=forms.widgets.TextInput(
#                                    attrs={'class': 'layui-input', 'placeholder': '请您输入手机号',
#                                           'lay-verify': 'required|phone', 'id': 'username'}), )
#     password = forms.CharField(max_length=20, label='请您输入密码',
#                                widget=forms.widgets.PasswordInput(
#                                    attrs={'class': 'layui-input', 'placeholder': '请您输入密码',
#                                           'lay-verify': 'required|password', 'id': 'password'}), )
#
#     # 自定义表单字段username的数据清洗
#     def clean_username(self):
#         if len(self.cleaned_data['username']) == 11:
#             return self.cleaned_data['username']
#         else:
#             raise ValidationError('用户名为手机号码')

# forms.Form表单类和模型实现数据交互最主要的问题是表单字段和模型字段的匹配，比如表单字段为CharFiled，而模型字段为IntegerField，那么两者在进行
# 数据交互的时候，程序可能会提示异常信息，但是将表单类Form改为ModleForm就无需考虑字段匹配问题了
class LoginModelForm(forms.ModelForm):
    class Meta:
        # model是ModelForm的特有属性，它将模型表单类与某个模型进行绑定
        model = User
        # fields是选取模型某类字段生成表单字段
        fields = ('username', 'password')
        # labels是为每个表单字段设置Html元素控件的label标签，以字典格式表示，每个键值对的键为表单字段名称，值为label标签的值
        labels = {
            'username': '请您输入账号',
            'password': '请您输入密码',
        }
        # 设置表单字段的错误信息__all__标识所有表单字段的错误信息
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
        }
        # 定义widgets，设置表单字段对应HTML元素控件的属性
        widgets = {
            'username': forms.widgets.TextInput(
                                   attrs={'placeholder': '请您输入账号','id': 'username'}),
            'password': forms.widgets.PasswordInput(
                                   attrs={'placeholder': '请您输入密码','id': 'password'})
        }

    # 自定义表单字段username的数据清洗
    def clean_username(self):
        if (self.cleaned_data['username']).isalpha():
            return self.cleaned_data['username']
        else:
            raise ValidationError('用户名为姓名英文全拼')
