# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-7-6 下午12:57'
from django import forms

from .models import Food, FoodCategory


# 用于处理文件的上传
class FoodForm(forms.ModelForm):
    class Meta:
        # 指定model
        model = Food
        # 指定想要修改的字段
        fields = ['cover_image','title','description', 'link','category','tags']