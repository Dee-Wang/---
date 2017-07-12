from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from actions.utils import create_action
from constants import *

from .models import FoodTopic
from .forms import TopicForm
# from operation.models import FoodInTopic
from food.models import Food


# 话题列表
class TopicListView(View):
    def get(self, request):
        all_topics = FoodTopic.objects.all()

        # 对所有的专题进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_topics, 6, request=request)
        topics = p.page(page)
        return render(request, "topic/topic_list.html", {
            'all_topics':all_topics,
            'topics':topics,
        })


# 话题详情
class TopicDetailView(View):
    def get(self, request, topic_id):
        cur_topic = FoodTopic.objects.get(id=int(topic_id))

        # cur_topic_food = cur_topic.foodintopic_set.all()
        # cur_topic_food = FoodInTopic.objects.filter(topic=cur_topic)
        # food_ids = [topic_food.food.id for topic_food in cur_topic_food]
        # all_topic_food = Food.objects.filter(id__in=food_ids)
        all_topic_food = cur_topic.food.all()



        return render(request, "topic/topic_detail.html", {
            'topic':cur_topic,
            # 'cur_topic_food': cur_topic_food,
            'all_topic_food':all_topic_food,
        })


# 创建新的专题
class TopicCreateView(View):
    def get(self, request):
        form = TopicForm()
        # categorys = FoodCategory.objects.all()
        foods = Food.objects.all()
        return render(request, "topic/topic_create.html", {
            'form':form,
            'foods':foods,
        })

    def post(self, request):
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            form.save_m2m()
            create_action(request.user, SHARE, topic)
            return HttpResponseRedirect(reverse('topic:topiclist'))
        else:
            # categorys = FoodCategory.objects.all()
            foods = Food.objects.all()
            return render(request, "topic/topic_create.html", {
                'form': form,
                'foods': foods,
            })