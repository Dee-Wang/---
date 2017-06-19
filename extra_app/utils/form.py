# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-19 上午10:35'

from django import forms
from django.core.validators import RegexValidator


# 写一个方法来规定输入的密码的格式
def RegexPasswordField(label):
    return forms.CharField(
        label=label,
        validators=[
            RegexValidator('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d#?!@$%^&*+-]{6,32}$', message="密码长度不少于6并且至少包含一个字母和数字")
        ],
        widget=forms.PasswordInput
    )