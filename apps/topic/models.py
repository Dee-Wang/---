from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse

from user.models import UserProfile
from food.models import Food
# Create your models here.


# 食物专题信息
class FoodTopic(models.Model):
    title = models.CharField(max_length=32, verbose_name='专题名称')
    cover_image = models.ImageField(upload_to='topic/cover/%Y/%m/%d', verbose_name='封面图片', default="image/foodtopic.jpg")
    description = models.TextField(verbose_name='专题描述')
    total_collects = models.PositiveIntegerField(db_index=True, default=0, verbose_name='收藏数')
    tags = models.CharField(max_length=64, default='', verbose_name='专题标签')
    food = models.ManyToManyField(Food, related_name='topics_belong', verbose_name='包含美食')
    user = models.ForeignKey(UserProfile, related_name='topics_shared', verbose_name='创建用户', blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.title

    # # 获取专题详情的界面的URL地址
    # def get_absolute_url(self):
    #     return reverse('topic:topicdetail', kwargs={'topic_id':self.id})

    class Meta:
        verbose_name = "美食专题"
        verbose_name_plural = verbose_name
