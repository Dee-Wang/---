from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse

from location.models import City
# Create your models here.


# 继承AbstractUser的用户类
class User(AbstractUser):
    # 继承AbstractUser类，并且对其做出扩展，新增我的关注
    following = models.ManyToManyField('self', related_name="followers", blank=True, symmetrical=False, verbose_name="我在关注")

    def __str__(self):
        return self.username


# 用户信息数据表
class UserProfile(models.Model):
    # 这里和上面的User表是一对一的关系，每一个用户都会有一个用户信息，一个用户信息也只对应一个用户
    user = models.OneToOneField(User, related_name="followers", on_delete=models.CASCADE, verbose_name="用户")
    nickname = models.CharField(max_length=16, verbose_name="昵称", default="")
    location = models.ForeignKey(City, null=True, blank=True, verbose_name='居住城市')
    introduction = models.TextField(max_length=1024, blank=True, verbose_name='个人简介')
    gender = models.CharField(max_length=2, choices=[('m', '男'), ('f', '女')], null=True, blank=True, verbose_name='性别')
    birthday = models.DateTimeField(verbose_name="出生日期", null=True, blank=True)
    avatar = models.ImageField(max_length=128, upload_to='users/avatar/%Y/%m/%d', verbose_name='头像',default="image/superman.jpg")

    def __str__(self):
        return "{}的信息".format(self.user.username)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


# 用户设置数据表
class UserSettings(models.Model):
    # 和上面一样，每一个用户对应一个用户设置，每一个用户设置也只对应一个用户，这里是一对一的关系
    user = models.OneToOneField(User, related_name="followers", on_delete=models.CASCADE, verbose_name="用户")
    backgground_img = models.ImageField(max_length=256, upload_to='user/background_img/%Y/%m/%d', blank=True, null=True, verbose_name="主页背景")

    def __str__(self):
        return "{}的设置".format(self.user.username)

    class Meta:
        verbose_name = "用户设置"
        verbose_name_plural = verbose_name
