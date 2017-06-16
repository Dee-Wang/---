from django.db import models

from user.models import UserProfile

# Create your models here.
# # 用户和用户之间的关注和被关注的关系
# class UserFollowUser(models.Model):
#     # 这里暂且以star和fans来形容这种关注和被关注的关系
#     star = models.ForeignKey(UserProfile, verbose_name="被关注的人")
#     fans = models.ForeignKey(UserProfile, verbose_name="追随者")
#
#     def __str__(self):
#         return '{0}在关注({1})'.format(self.fans.username,self.star.username)
#
#     class Meta:
#         verbose_name = "关注与被关注"
#         verbose_name_plural = verbose_name
