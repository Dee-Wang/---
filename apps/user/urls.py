# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-19 上午10:25'
from django.conf.urls import url

from .views import LoginView, RegisterView, ActiveView, LogoutView, UserFollowingView, UserShareView
from .views import TopicCollectionView, UserIndexView, UserSettingView, UserHaveEatedView, UserFollowerView, UserWantEatView

urlpatterns = [
    # 用户登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),

    # 用户登出页面
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    #
    # 用户注册页面
    url(r'^register/$', RegisterView.as_view(), name="register"),
    #
    # 用户激活页面
    url(r'^active_user/(?P<active_code>.*)/$', ActiveView.as_view(), name="active_user"),

    # 当前用户在关注谁
    url(r'^userfollowing/$', UserFollowingView.as_view(), name="userfollowing"),

    # 当前用户的粉丝
    url(r'^userfollower/$', UserFollowerView.as_view(), name="userfollower"),

    # 用户收藏的专题
    url(r'^topiccollection/$', TopicCollectionView.as_view(), name='topiccollection'),

    # 用户首页
    url(r'^userindex/(?P<user_id>\d+)/$', UserIndexView.as_view(), name='userindex'),

    # 用户设置,包括用户的个人信息设置和用户的背景图片的设置
    url(r'^usersetting/$', UserSettingView.as_view(), name='usersetting'),

    # 用户吃过的食物列表
    url(r'^usereated/$', UserHaveEatedView.as_view(), name='usereated'),

    # 用户想吃的食物列表
    url(r'^userwanteat/$', UserWantEatView.as_view(), name='userwanteat'),

    # 用户分享
    url(r'^usershare/$', UserShareView.as_view(), name='usershare'),
]