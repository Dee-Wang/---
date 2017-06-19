from django.shortcuts import render
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm


# 网站首页
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


# 用户登录
def user_login(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_authenticated_user()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {
        'form': form,
    })
# class LoginView(View):
    # def get(self, request):
    #     return render(request, "login.html", {})
    # def post(self, request):
    #     login_form = LoginForm(request.POST)
    #     if login_form.is_valid():
    #         user_name = request.POST.get("username", "")
    #         pass_word = request.POST.get("password", "")
    #         user = authenticate(username = user_name, password = pass_word)
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponseRedirect(reverse('index'))
    #                 # return render(request, "index.html")
    #             else:
    #                 return render(request, "login.html", {"msg": "用户未激活"})
    #         else:
    #             return render(request, "login.html", {"msg":"用户名或者密码错误"})
    #     else:
    #         return render(request, "login.html", { "login_form": login_form})


# 用户注册
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.get_authenticated_user()
            login(request, user)
            return HttpResponseRedirect(reverse('user/login'))
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {
            'form': form
        })

