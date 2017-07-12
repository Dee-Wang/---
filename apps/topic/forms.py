# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-7-11 下午1:08'

from django import forms
from .models import FoodTopic


# 创建一个专题的表单
class TopicForm(forms.ModelForm):
    class Meta:
        model = FoodTopic
        fields = ['title','cover_image','description', 'tags', 'food']