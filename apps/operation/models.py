from datetime import datetime

from django.db import models

from food.models import Food
from user.models import UserProfile
from forum.models import ForumPost
from topic.models import FoodTopic


# 用户想吃什么食物
class UserWantEat(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    food = models.ForeignKey(Food, verbose_name="想吃的食物")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return "{0}想吃{1}".format(self.user.username, self.food.title)

    class Meta:
        verbose_name = "用户想吃的食物"
        verbose_name_plural = verbose_name


# 用户吃过的食物
class UserHaveAte(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    food = models.ForeignKey(Food, verbose_name="吃过的食物")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return "{0}吃过{1}".format(self.user.username, self.food.title)

    class Meta:
        verbose_name = "用户吃过的食物"
        verbose_name_plural = verbose_name


# 用户推荐的帖子
class UserRecommendForum(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    forum = models.ForeignKey(ForumPost, verbose_name="推荐的帖子")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return "{0}推荐{1}".format(self.user.username, self.forum.forum_title)

    class Meta:
        verbose_name = "用户推荐的帖子"
        verbose_name_plural = verbose_name


# 用户收藏的专题
class UserCollectTopic(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    topic = models.ForeignKey(FoodTopic, verbose_name="收藏的专题")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return "{0}收藏{1}".format(self.user.username, self.topic.title)

    class Meta:
        verbose_name = "用户收藏的专题"
        verbose_name_plural = verbose_name


# 专题和食物之间的关系
class FoodInTopic(models.Model):
    food = models.ForeignKey(Food, verbose_name="美食")
    topic = models.ForeignKey(FoodTopic, verbose_name="所属专题")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return "{0}在专题{1}中".format(self.food.title, self.topic.title)

    class Meta:
        verbose_name = "食物和专题"
        verbose_name_plural = verbose_name



