# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-19 上午10:25'
from django.conf.urls import url

from .views import LoginView, RegisterView, ActiveView, LogoutView, UserInfoView, UserFollowingView, UserShareView
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
    url(r'^userindex/$', UserIndexView.as_view(), name='userindex'),

    # 用户设置,包括用户的个人信息设置和用户的背景图片的设置
    url(r'^usersetting/$', UserSettingView.as_view(), name='usersetting'),

    # 用户吃过的食物列表
    url(r'^usereated/$', UserHaveEatedView.as_view(), name='usereated'),

    # 用户想吃的食物列表
    url(r'^userwanteat/$', UserWantEatView.as_view(), name='userwanteat'),

    # 用户分享
    url(r'^usershare/$', UserShareView.as_view(), name='usershare'),
    #
    # # 用户忘记密码界面
    # url(r'^forget_pwd/', ForgetPasswordView.as_view(), name="forget_pwd"),
    #
    # # 用户跳转到重置密码的页面
    # url(r'^reset_pwd/(?P<active_code>.*)/$', ResetPasswordView.as_view(), name="reset_pwd"),
    #
    # # 用户跳转到重置密码的页面的之后，在该页面修改密码，提交表单信息
    # url(r'^modify_pwd/', ModifyPasswordView.as_view(), name="modify_pwd"),
    #
    # 显示用户个人信息的界面
    url(r'^userinfo/$', UserInfoView.as_view(), name="userinfo"),
    #
    # # 用户修改除了头像，密码和邮箱之外的信息
    # url(r'^modify_info/$', ModifyPersonalInfoView.as_view(), name="modify_info"),
    #
    # # 用户修改个人头像页面
    # url(r'^image/upload/$', UploadImageView.as_view(), name="image/upload"),
    #
    # # # 用户修改个人密码页面
    # # url(r'^changepwd/$', ChangePasswordView.as_view(), name="changepwd"),
    #
    # # 用户修改个人密码页面
    # url(r'^changepwd/$', UpdatePwdView.as_view(), name="changepwd"),
    #
    # # 发送邮箱验证码
    # url(r'^sendemailcode/$', SendEmailCodeView.as_view(), name="sendemailcode"),
    #
    # # 登陆之后修改邮箱的时候验证验证码
    # url(r'^updateemail/$', UpdateEmailView.as_view(), name="updateemail"),
    #
    # # 我的课程列表页面
    # url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    #
    # # 我的收藏课程列表页面
    # url(r'^myfavcourse/$', UserFavCourseView.as_view(), name="myfavcourse"),
    #
    # # 我的收藏讲师列表页面
    # url(r'^myfavteacher/$', UserFavTeacherView.as_view(), name="myfavteacher"),
    #
    # # 我的收藏机构列表页面
    # url(r'^myfavorg/$', UserFavOrgView.as_view(), name="myfavorg"),
    #
    # # 用户消息列表页面
    # url(r'^usermessage/$', UserMessageView.as_view(), name="usermessage"),
]