# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-21 下午4:52'
from django.conf.urls import url

from .views import TopicListView, TopicDetailView

urlpatterns = [
    # 话题列表
    url(r'^topiclist/$', TopicListView.as_view(), name='topiclist'),

    # 话题详情
    url(r'^topicdetail/$', TopicDetailView.as_view(), name='topicdetail'),
]
