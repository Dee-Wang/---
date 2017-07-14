# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-19 上午10:25'
from django.conf.urls import url

from .views import LoginView, RegisterView, ActiveView, LogoutView, UserFollowingView, UserShareView
from .views import TopicCollectionView, UserIndexView, UserSettingView, UserHaveEatedView, UserFollowerView, UserWantEatView
from .views import FollowView, GetCityView

urlpatterns = [
    # 账户相关
    # 用户登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),
    # 用户登出页面
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    # 用户注册页面
    url(r'^register/$', RegisterView.as_view(), name="register"),
    # 用户激活页面
    url(r'^active_user/(?P<active_code>.*)/$', ActiveView.as_view(), name="active_user"),


    #用户个人信息相关
    # 当前用户在关注谁
    url(r'^userfollowing/(?P<user_id>\d+)/$', UserFollowingView.as_view(), name="userfollowing"),
    # 当前用户的粉丝
    url(r'^userfollower/(?P<user_id>\d+)/$', UserFollowerView.as_view(), name="userfollower"),
    # 用户收藏的专题
    url(r'^topiccollection/(?P<user_id>\d+)/$', TopicCollectionView.as_view(), name='topiccollection'),
    # 用户首页
    url(r'^userindex/(?P<user_id>\d+)/$', UserIndexView.as_view(), name='userindex'),
    # 用户设置,包括用户的个人信息设置和用户的背景图片的设置
    url(r'^usersetting/(?P<user_id>\d+)/$', UserSettingView.as_view(), name='usersetting'),
    # 用户吃过的食物列表
    url(r'^usereated/(?P<user_id>\d+)/$', UserHaveEatedView.as_view(), name='usereated'),
    # 用户想吃的食物列表
    url(r'^userwanteat/(?P<user_id>\d+)/$', UserWantEatView.as_view(), name='userwanteat'),
    # 用户分享的列表
    url(r'^usershare/(?P<user_id>\d+)/$', UserShareView.as_view(), name='usershare'),


    # 用户行为相关
    # 用户关注的动作
    url(r'^follow/$', FollowView.as_view(), name='follow'),
    # 根据省份获取城市
    url(r'^get_cities/$', GetCityView.as_view(), name='get_cities'),
]