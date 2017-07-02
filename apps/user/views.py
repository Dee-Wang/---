from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm,RegisterForm
from utils.email_send import send_email
from topic.models import FoodTopic


# 网站首页
class IndexView(View):
    def get(self, request):
        all_topics = FoodTopic.objects.all()

        return render(request, "index.html", {
            'all_topics':all_topics,
        })


# 用户登录的时候账户名可以是用户名，可以是用户的邮箱
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email= username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 用户登录
class LoginView(View):
    def get(self, request):
        return render(request, "user/login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username = user_email, password = pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, "user/login.html", {"msg": "用户未激活"})
            else:
                return render(request, "user/login.html", {"msg":"用户名或者密码错误"})
        else:
            return render(request, "user/login.html", { "login_form": login_form})


# 用户登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        # request.user.is_authenticated = False
        return HttpResponseRedirect(reverse('index'))


# 用户注册
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "user/register.html", {'register_form':register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username", "")
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            confirmPassword = request.POST.get("confirmPassword", "")
            if UserProfile.objects.filter(username = user_name):
                return render(request, "user/register.html", { "register_form": register_form, "msg": "用户已经存在" })
            elif UserProfile.objects.filter(email = email):
                return render(request, "user/register.html", { "register_form": register_form, "msg": "邮箱已经被注册" })
            elif password != confirmPassword:
                return render(request, "user/register.html", {"register_form": register_form, "msg": "两次输入的密码不一致"})
            else:
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.email = email
                user_profile.is_active = False
                user_profile.password = make_password(password)
                user_profile.save()

                send_email(email, "register")
                return render(request, "user/active_successfully.html")
        else:
            return render(request, "user/register.html", {"register_form": register_form, "msg": "填入的信息有误" })


# 用户激活
class ActiveView(View):
    def get(self,request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email = email)
                user.is_active = True
                user.save()
        else:
            return render(request, "user/active_fail.html")
        return HttpResponseRedirect(reverse('user:login'))


# 当前用户在关注谁
class UserFollowingView(View):
    def get(self, request):
        return render(request, "user/user_following.html")

# 当前用户在关注谁
class UserFollowerView(View):
    def get(self, request):
        return render(request, "user/user_follower.html")


# 用户收藏的话题
class TopicCollectionView(View):
    def get(self, request):
        return render(request, "user/topic_collection.html")


# 用户首页
class UserIndexView(View):
    def get(self, request):
        return render(request, "user/user_index.html")


# 用户设置，包括用户个人信息设置和用户背景图设置
class UserSettingView(View):
    def get(self, request):
        return render(request, "user/user_setting.html")


# 用户吃过的食物的列表
class UserHaveEatedView(View):
    def get(self, request):
        return render(request, "user/user_haveeated.html")


# 用户想吃的食物的列表
class UserWantEatView(View):
    def get(self, request):
        return render(request, "user/user_wanteat.html")


# 用户分享
class UserShareView(View):
    def get(self, request):
        return render(request, "user/user_share.html")


