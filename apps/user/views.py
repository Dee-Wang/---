from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib import messages

# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm,RegisterForm, ModifyUserInfoForm
from utils.email_send import send_email
from utils.mixin_utils import LoginRequiredMixin
from topic.models import FoodTopic
from actions.models import Action
from actions.utils import create_action
from food.models import Food
from constants import *
from operation.models import UserWantEat, UserHaveAte, UserCollectTopic, UserLikeFood, UserDislikeFood, UserRecommendForum
from location.models import Province, City, Store


# 网站首页
class IndexView(View):
    def get(self, request):
        all_topics = FoodTopic.objects.all()
        # cur_user = request.user

        return render(request, "index.html", {
            'all_topics':all_topics,
            # 'user':cur_user,
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
    def get(self, request, user_id):
        cur_user = UserProfile.objects.get(id=int(user_id))
        followings = cur_user.following.all()
        return render(request, "user/user_following.html", {
            'user':cur_user,
            'followings':followings,
        })


# 当前用户被谁关注
class UserFollowerView(View):
    def get(self, request, user_id):
        cur_user = UserProfile.objects.get(id=int(user_id))
        followers = cur_user.followers.all()
        return render(request, "user/user_follower.html", {
            'user':cur_user,
            'followers':followers,
        })


# 用户收藏的话题
class TopicCollectionView(View):
    def get(self, request, user_id):
        cur_user = UserProfile.objects.get(id=int(user_id))
        curuser_coll_topics = UserCollectTopic.objects.filter(user=cur_user)
        coll_topics_list = []
        for user_coll_topic in curuser_coll_topics:
            coll_topic = FoodTopic.objects.get(id=user_coll_topic.topic_id)
            coll_topics_list.append(coll_topic)
        return render(request, "user/topic_collection.html", {
            'user':cur_user,
            'collections':coll_topics_list,
        })


# 用户个人首页的部分
class UserIndexView(View):
    def get(self, request, user_id):
        cur_user = UserProfile.objects.get(id=int(user_id))
        recent_actions = Action.objects.filter(user=cur_user).all()[:10]
        return render(request, "user/user_index.html", {
            'user':cur_user,
            'actions':recent_actions,
        })


# 用户修改和人的信息
class UserSettingView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        provinces = Province.objects.all()
        cities = City.objects.all()
        cur_user = UserProfile.objects.get(id=int(user_id))
        form = ModifyUserInfoForm(instance=cur_user)
        return render(request, "user/user_setting.html", {
            'user':cur_user,
            'form':form,
            'provinces':provinces,
            'cities':cities,
        })

    def post(self, request, user_id):
        provinces = Province.objects.all()
        cities = City.objects.all()
        cur_user = UserProfile.objects.get(id=int(user_id))
        form = ModifyUserInfoForm(instance=cur_user, data=request.POST, files=request.FILE)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            form.save_m2m()
            messages.success(request, PROFILE_UPDATE_SUCCESS)
        else:
            messages.error(request, PROFILE_UPDATE_FAIL)
        return render(request, "user/user_setting.html", {
            'user':cur_user,
            'form':form,
            'provinces': provinces,
            'cities': cities,
        })




# 用户吃过的食物的列表
class UserHaveEatedView(View):
    def get(self, request, user_id):
        cur_user = UserProfile.objects.get(id=int(user_id))
        curuser_ate_food = UserHaveAte.objects.filter(user=cur_user)
        user_atefood_list = []
        for ate_food in curuser_ate_food:
            user_ate_food = Food.objects.get(id=ate_food.food_id)
            user_atefood_list.append(user_ate_food)

        return render(request, "user/user_haveeated.html", {
            'user':cur_user,
            'foods':user_atefood_list,
        })


# 用户想吃的食物的列表
class UserWantEatView(View):
    def get(self, request, user_id):
        cur_user = UserProfile.objects.get(id=int(user_id))
        curuser_want_food = UserWantEat.objects.filter(user=cur_user)
        user_wantfood_list = []
        for want_food in curuser_want_food:
            user_want_food = Food.objects.get(id=want_food.food_id)
            user_wantfood_list.append(user_want_food)
        return render(request, "user/user_wanteat.html", {
            'user':cur_user,
            'foods':user_wantfood_list,
        })


# 用户分享的信息
class UserShareView(View):
    def get(self, request, user_id):
        cur_user = UserProfile.objects.get(id=int(user_id))
        all_food = Food.objects.all()
        cur_user_foods = all_food.filter(user=cur_user)
        return render(request, "user/user_share.html", {
            'user':cur_user,
            'foods':cur_user_foods,
        })


# 用户关注其他用户的动作
class FollowView(LoginRequiredMixin, View):
    def post(self, request):
        cur_user = request.user
        user_id = int(request.POST.get('id', ''))
        action = request.POST.get('action', '')
        if user_id and action:
            user = UserProfile.objects.get(pk=user_id)
            if action == 'follow':
                cur_user.following.add(user)
                create_action(cur_user, FOLLOW, user)
            elif action == 'unfollow':
                cur_user.following.remove(user)
            else:
                return JsonResponse(JSON_FAIL(STATUS_INVALID_ARGUMENTS))
            return JsonResponse({'status':True})
        return JsonResponse(JSON_FAIL(STATUS_INVALID_ARGUMENTS), status=400)


# 获取当前用户所在的城市
class GetCityView(View):
    def get(self, request):
        province = request.GET.get('province')
        cities = City.objects.filter(province__province_name=province).values_list('id', 'name')
        return JsonResponse(list(cities), safe=False)



