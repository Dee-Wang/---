# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-21 下午4:52'
from django.conf.urls import url

from .views import TopicListView, TopicDetailView, TopicCreateView

urlpatterns = [
    # 话题列表
    url(r'^topiclist/$', TopicListView.as_view(), name='topiclist'),

    # 话题详情
    url(r'^topicdetail/(?P<topic_id>\d+)/$', TopicDetailView.as_view(), name='topicdetail'),

    # 创建话题
    url(r'^topiccreate/$', TopicCreateView.as_view(), name='topiccreate'),
]
