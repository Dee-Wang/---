from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response


# 食物发布
class FoodCreateView(View):
    def get(self, request):
        return render(request, "food/food_create.html", {})


# 食物详情
class FoodDetailView(View):
    def get(self, request):
        return render(request, "food/food_detail.html", {})


# 发现食物
class FoodExploreView(View):
    def get(self, request):
        return render(request, "food/food_explore.html", {})


