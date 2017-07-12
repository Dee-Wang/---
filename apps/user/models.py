from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser

from location.models import City


# 用户信息数据表
class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=16, verbose_name="昵称", default="")
    location = models.ForeignKey(City, null=True, blank=True, verbose_name='居住城市')
    introduction = models.TextField(max_length=1024, blank=True, null=True, verbose_name='个人简介')
    gender = models.CharField(max_length=8, choices=(("male", "先生"), ("female", "女士")), default="male", verbose_name="性别")
    birthday = models.DateTimeField(verbose_name="出生日期", null=True, blank=True)
    phone_num = models.CharField(max_length=11, verbose_name="手机号码", null=True, blank=True)
    image = models.ImageField(max_length=128, upload_to='users/avatar/%Y/%m/%d', verbose_name='头像',default="image/superman.jpg")
    email = models.CharField(max_length=32, verbose_name="个人邮箱", default="")
    total_wantnum = models.PositiveIntegerField(default=0, verbose_name="用户想吃的美食的总数")
    total_likenum = models.PositiveIntegerField(default=0, verbose_name="用户吃过的美食的总数")
    following = models.ManyToManyField('self', blank=True, related_name='followers', symmetrical=False, verbose_name="关注与被关注")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user:userindex', kwargs={'user_id':self.id})

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


# 使用邮箱注册以后，向注册邮箱发送验证码，验证用户的身份，完成用户的验证和激活
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=16, verbose_name="验证码")
    email = models.CharField(max_length=32, verbose_name="邮箱")
    send_type = models.CharField(max_length=64, choices=(("register","注册"), ("forget_password","忘记密码"),("change_email","修改邮箱")), default="register", verbose_name="验证类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

