# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-21 下午4:40'
from django.conf.urls import url

from .views import ForumIndexView


urlpatterns = [
    # 帖子首页
    url(r'^forumindex/$', ForumIndexView.as_view(), name='forumindex'),
]