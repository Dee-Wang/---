from datetime import datetime

from django.db import models
from updown.fields import RatingField

from user.models import UserProfile


# 食物的分类
class FoodCategory(models.Model):
    category_name = models.CharField(max_length=64, verbose_name="食品种类", default="好吃的")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "食品种类"
        verbose_name_plural = verbose_name


# 食物信息
class Food(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    food_name = models.CharField(max_length=128, verbose_name="食品名称", default="")
    description = models.TextField(verbose_name='描述')
    cover_image = models.ImageField(max_length=128, upload_to='food/cover/%Y/%m/%d', verbose_name='封面图片',default="image/dangao.jpg")
    rating = RatingField(can_change_vote=True)
    # 想要吃这个食物的用户，这里使用的ManyToManyField，为用户和食物建立了一个多对多的表，也就是一个用户可以想要吃多个食物，一个食物也可以被多个人喜欢
    users_wta = models.ManyToManyField(UserProfile, related_name='foods_wta', blank=True, verbose_name='想吃的用户')
    # 和上面的类似，只不过表示的是吃过的
    users_ate = models.ManyToManyField(UserProfile, related_name='foods_ate', blank=True, verbose_name='吃过的用户')
    link = models.URLField(verbose_name='相关链接', max_length=200, null=True, blank=True)
    category = models.ForeignKey(FoodCategory, verbose_name='分类')
    user = models.ForeignKey(UserProfile, related_name='foods_shared', verbose_name='创建用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    tags = models.CharField(max_length=64, default='', verbose_name='食物标签')

    def __str__(self):
        return self.food_name

    class Meta:
        verbose_name = "食物信息"
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)