# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-7-6 下午2:15'
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# 自己定义验证用户是否登录的视图函数
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/user/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)