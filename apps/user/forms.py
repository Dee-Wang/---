# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-19 上午10:49'

from django import forms

from captcha.fields import CaptchaField

from .models import UserProfile


# 用户登陆的表单
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


# 用户注册的表单
class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    confirmPassword = forms.CharField(required=True, min_length=6)
    # captcha = CaptchaField()


# 用户修改个人信息的表单
class ModifyUserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'gender', 'birthday', 'location', 'introduction']
        widgets = {
            'birthday': forms.SelectDateWidget(years=range(1950,2017), attrs={'class':'selections'})
        }