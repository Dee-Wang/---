from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse


# 话题列表
class TopicListView(View):
    def get(self, request):
        return render(request, "topic/topic_list.html", {})


# 话题详情
class TopicDetailView(View):
    def get(self, request):
        return render(request, "topic/topic_detail.html", {})
