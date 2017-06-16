from django.db import models

from user.models import UserProfile
from food.models import Food
# Create your models here.

class FoodTopic(models.Model):
    title = models.CharField(max_length=32, verbose_name='专题名称')
    cover_image = models.ImageField(upload_to='topic/cover/%Y/%m/%d', verbose_name='封面图片', default="image/foodtopic.jpg")
    description = models.TextField(verbose_name='专题描述')
    users_collect = models.ManyToManyField(UserProfile, related_name='topics_collected', blank=True, verbose_name='收藏的用户')
    total_collects = models.PositiveIntegerField(db_index=True, default=0, verbose_name='收藏数')
    foods = models.ManyToManyField(Food, related_name='topics_belong', verbose_name='美食')
    tags = models.CharField(max_length=64, default='', verbose_name='专题标签')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "美食专题"
        verbose_name_plural = verbose_name
