# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-19 上午10:49'
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied

from .models import UserProfile, UserSetting

from utils.form import RegexPasswordField


# # 用户登录的表单
# class LoginForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, min_length=6)


# 获取当前处于登录状态的用户
class UserCacheMixin(object):
    def __init__(self, *args, **kwargs):
        self.user_cache = None

    def get_authenticated_user(self):
        return self.user_cache


# 用户登录用的表单,这里在forms里面对用户输入的信息进行了验证
class LoginForm(forms.ModelForm, UserCacheMixin):
    password = forms.CharField(label="密码", widget=forms.PasswordInput)

    # 获取request中的用户登录名和密码的数据
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('用户名或者密码不正确')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('用户已经被锁定')

        return self.cleaned_data

    class Meta:
        model = UserProfile
        fields = ('username', 'password')


# 用户注册用的表单
class RegisterForm(forms.ModelForm, UserCacheMixin):
    password = RegexPasswordField('密码')
    confirm_password = RegexPasswordField('确认密码')

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if username and email and password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('两次输入的密码不一致')
            elif UserProfile.objects.filter(username=username).exists():
                raise forms.ValidationError('该用户已经存在')
            elif UserProfile.objects.filter(email=email).exists():
                raise forms.ValidationError('该邮箱已被注册')

            UserProfile.objects.create_user(username=username, email=email, password=password)
            self.user_cache = authenticate(username=username, password=password)

        return self.cleaned_data

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'confirm_password')