from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from constants import *

from user.models import UserProfile


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