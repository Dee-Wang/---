from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Food, FoodCategory


# 食物列表
class FoodListView(View):
    def get(self, request):
        all_food = Food.objects.all()
        all_category = FoodCategory.objects.all()

        category = request.GET.get('category', '')

        if category:
            for cur_category in all_category:
                if category == cur_category.category_name:
                    cur_category_food = cur_category.food_set.all()
        else:
            cur_category_food = all_food


        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(cur_category_food, 3, request=request)
        food_page = p.page(page)
        return render(request, "food/food_list.html", {
            'category':category,
            'all_food':all_food,
            'all_category':all_category,
            'cur_category_food':cur_category_food,
            'food_page':food_page,
        })


# 食物详情
class FoodDetailView(View):
    def get(self, request, food_id):
        all_food = Food.objects.all()
        cur_food = Food.objects.get(id=int(food_id))
        return render(request, "food/food_detail.html", {
            'all_food':all_food,
            'cur_food':cur_food,
        })


# 食物发布
class FoodCreateView(View):
    def get(self, request):
        return render(request, "food/food_create.html", {})


# 发现食物
class FoodExploreView(View):
    def get(self, request):
        """
        这里我们展示9张图片，选择方式有两种，一种是默认的按照发布时间排序，越新的排在前面.
        还一种方式是按照受欢迎的程度进行排序，越受欢迎的排在前面，但是最后都选择前9个
        """
        all_food = Food.objects.all()

        # 根据发布时间排序，选择最新的9个
        sort = request.GET.get('sort','')

        if sort:
            # 按照发布时间排序
            if sort == 'new':
                sorted_food = all_food.order_by("-add_time")
            elif sort == 'hot':
                sorted_food = all_food.order_by("-total_likenum")
        else:
            sorted_food = all_food

        display_food = sorted_food[:9]

        return render(request, "food/food_explore.html", {
            'sort':sort,
            'all_food':all_food,
            'display_food':display_food,
        })





