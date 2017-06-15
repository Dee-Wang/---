from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from location.models import City
# Create your models here.


# 用户信息数据表
class UserProfile(models.Model):
    nickname = models.CharField(max_length=16, verbose_name="昵称", default=" ")
    location = models.ForeignKey(City, null=True, blank=True, verbose_name='居住城市')
    introduction = models.TextField(max_length=1024, blank=True, verbose_name='个人简介')
    gender = models.CharField(max_length=2, choices=[('m', '男'), ('f', '女')], null=True, blank=True, verbose_name='性别')
    birthday = models.DateTimeField(verbose_name="出生日期", null=True, blank=True)
    avatar = models.ImageField(max_length=128, upload_to='users/avatar/%Y/%m/%d', verbose_name='头像',default="image/superman.jpg")