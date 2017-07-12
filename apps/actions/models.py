from datetime import datetime

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone

from constants import *

from user.models import UserProfile


# 前面和后面的内容分别指的是什么呢？
action_classes = {
    SHARE: 'fa-share-alt',
    LIKE: 'fa-thumbs-up',
    COLLECT: 'fa-bookmark',
    FOLLOW: 'fa-eye',
    COMMENT: 'fa-comment',
    WTA: 'fa-cutlery',
    ATE: 'fa-hand-peace-o',
    POST: 'fa-send'
}


# 创建行为的基类
class Action(models.Model):
    user = models.ForeignKey(UserProfile, related_name='actions', db_index=True, verbose_name='用户')
    verb = models.CharField(max_length=255, verbose_name='活动描述')
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', verbose_name='活动对象的类型')
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True, verbose_name='活动对象id')
    target = GenericForeignKey('target_ct', 'target_id')
    add_time = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="活动时间")

    def __str__(self):
        return self.user.username + self.verb + self.target_ct.app_label

    # 获取对应的动作
    def get_action_class(self):
        return action_classes.get(self.verb, "")

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = verbose_name