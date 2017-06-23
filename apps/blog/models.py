from datetime import datetime

from django.db import models

from user.models import UserProfile

# Create your models here.


# 发布的信息的具体内容,这里理解成博文
class Blog(models.Model):
    blog_title = models.CharField(max_length=128, verbose_name='标题', default="")
    blog_user = models.ForeignKey(UserProfile, related_name='Release_posts', verbose_name='发布者')
    blog_content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = "博文信息"
        verbose_name_plural = verbose_name