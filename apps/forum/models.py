from datetime import datetime

from django.db import models

from user.models import UserProfile
# Create your models here.


# 板块信息
class Board(models.Model):
    board_creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='创建者')
    board_name = models.CharField(max_length=32, verbose_name='名称', default=" ")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.board_name

    class Meta:
        verbose_name = "板块信息"
        verbose_name_plural = verbose_name


# 帖子信息
class ForumPost(models.Model):
    forum_title = models.CharField(max_length=64, verbose_name='帖子标题', default="")
    forum_content = models.TextField(max_length=5096, verbose_name='帖子内容')
    forum_creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='创建者')
    board = models.ForeignKey(Board, blank=True, null=True, verbose_name='所属板块')
    created_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')
    users_like = models.ManyToManyField(UserProfile, related_name='forumposts_liked', blank=True, verbose_name='推荐的用户')
    total_likes = models.IntegerField(default=0, verbose_name='推荐数')

    def __str__(self):
        return self.forum_title

    class Meta:
        verbose_name = "帖子信息"
        verbose_name_plural = verbose_name