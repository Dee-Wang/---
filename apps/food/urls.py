# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-21 下午5:22'

from django.conf.urls import url


from .views import FoodCreateView, FoodDetailView, FoodExploreView, FoodListView

urlpatterns = [
    # 食物推荐发表
    url(r'^foodcreate/$', FoodCreateView.as_view(), name='foodcreate'),

    # 食物详情
    url(r'^fooddetail//(?P<food_id>\d+)/$', FoodDetailView.as_view(), name='fooddetail'),

    # 发现食物
    url(r'^foodexplore/$', FoodExploreView.as_view(), name='foodexplore'),

    # 食物列表
    url(r'^foodlist/$', FoodListView.as_view(), name='foodlist'),
]