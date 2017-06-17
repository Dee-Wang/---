from datetime import datetime

from django.db import models

from user.models import UserProfile
from food.models import Food
from topic.models import FoodTopic
from forum.models import Board, ForumPost
from blog.models import Blog


# 创建一个抽象类用户评论，下面具体项目的评论都继承自这个类，然后添加各自的评论的对象
class UserComment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='评论用户')
    content = models.TextField(max_length=512, verbose_name='评论内容')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    def __str__(self):
        return "{0}的评论是({1})".format(self.user.username, self.content)

    class Meta:
        abstract = True
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name


# 对美食的评价，继承上面的抽象类，填充评论的对象内容
class FoodComment(UserComment):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="comments", verbose_name="美食")

    class Meta:
        verbose_name = "美食评价"
        verbose_name_plural = verbose_name


# 对专题的评论， 继承上面的抽象类，填充评论的对象内容
class TopicComment(UserComment):
    topic = models.ForeignKey(FoodTopic, on_delete=models.CASCADE, related_name="comments", verbose_name="专题")

    class Meta:
        verbose_name = "专题评价"
        verbose_name_plural = verbose_name


# 对板块的评论，继承上面的抽象类，填充评论的对象内容
class BoardComment(UserComment):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="comments", verbose_name="板块")

    class Meta:
        verbose_name = "板块评价"
        verbose_name_plural = verbose_name


# 对帖子的评论， 继承上面的抽象类，填充评论的对象内容
class ForumComment(UserComment):
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name="comments", verbose_name="帖子")

    class Meta:
        verbose_name = "帖子评价"
        verbose_name_plural = verbose_name


# 对博文的评论， 继承上面的抽象类，填充评论的对象内容
class ForumComment(UserComment):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", verbose_name="博文")

    class Meta:
        verbose_name = "博文评价"
        verbose_name_plural = verbose_name
