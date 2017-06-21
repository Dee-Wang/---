"""chihuoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from user.views import IndexView

urlpatterns = [

    # 后台管理页面url
    url(r'^admin/', admin.site.urls),

    # 首页URL配置
    url('^$', IndexView.as_view(), name="index"),

    # 用户相关的url
    url(r'^user/', include('user.urls', namespace="user")),

    # 帖子
    url(r'^forum/', include('forum.urls', namespace="forum")),

    # 专题
    url(r'^topic/', include('topic.urls', namespace="topic")),

    # 食物
    url(r'^food/', include('food.urls', namespace="food")),

    # 验证码部分
    url(r'^captcha/', include('captcha.urls')),

    ]
