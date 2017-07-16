# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-7-16 下午11:44'
from django import forms

from .models import FoodComment, TopicComment, BoardComment, ForumComment


# 设计用户对美食评价的表单
class FoodCommentsForm(forms.ModelForm):

    class Meta:
        model = FoodComment
        fields = ['content']
