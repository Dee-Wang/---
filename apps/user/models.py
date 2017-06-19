from django.db import models
from django.contrib.auth.models import AbstractUser

from location.models import City
# Create your models here.


# class User(AbstractUser):
#     following = models.ManyToManyField('self',null=True, blank=True, related_name='followers', symmetrical=False)
#     def __str__(self):
#         return self.username


# 用户信息数据表
class UserProfile(AbstractUser):
    # user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16, verbose_name="昵称", default=" ")
    location = models.ForeignKey(City, null=True, blank=True, verbose_name='居住城市')
    introduction = models.TextField(max_length=1024, blank=True, null=True, verbose_name='个人简介')
    gender = models.CharField(max_length=8, choices=(("male", "先生"), ("female", "女士")), default="male", verbose_name="性别")
    birthday = models.DateTimeField(verbose_name="出生日期", null=True, blank=True)
    avatar = models.ImageField(max_length=128, upload_to='users/avatar/%Y/%m/%d', verbose_name='头像',default="image/superman.jpg")
    # background_image = models.ImageField(max_length=256, upload_to='user/background_img/%Y/%m/%d', blank=True, null=True, verbose_name="主页背景")
    following = models.ManyToManyField('self', blank=True, related_name='followers', symmetrical=False, verbose_name="关注与被关注")
    email = models.CharField(max_length=32, verbose_name="个人邮箱", default=" ")

    def __str__(self):
        return "{}的信息".format(self.username)

    # 获取当前用户关注的所有的用户
    def get_all_followings(self):
        return self.following.all()

    # 获取当前用户关注的所有用户的数量
    def get_following_num(self):
        return self.following.all().count()

    # 获取关注当前用户的所有用户
    def get_allfollowers(self):
        return self.followers.all()

    # 获取关注当前用户的数量
    def get_followers_num(self):
        return self.followers.all().count()

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class UserSetting(models.Model):
    user = models.OneToOneField(UserProfile, related_name='settings', on_delete=models.CASCADE)
    background_image = models.ImageField(max_length=256, upload_to='user/background_img/%Y/%m/%d', blank=True, null=True, verbose_name="主页背景")

    def __str__(self):
        return "{}的设置".format(self.user.username)

    class Meta:
        verbose_name = '用户设置'
        verbose_name_plural = '用户设置'

