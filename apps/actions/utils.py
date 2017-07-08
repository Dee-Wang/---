# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-7-8 下午7:00'

import datetime

from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action


# 描述创建一个项目这种行为
def create_action(user, verb, target=None):
    now = timezone.now()
    last_miunte = now - datetime.timedelta(seconds=120)
    # 做一个判断，如果传来的要创建的目标是合法的，并且之前这个事物没有被创项目，就新创建这个项目
    # 这里保留一个问题就是add_time__get,这里的__get有什么作用，是截止时间的意思吗？
    # 个人觉得在这里，没必要设置这样一个参数，我们就直接取出当前数据库里面的内容，还是说如果我们在存储过程中，另一个用户创建了这个项目该怎么处理呢
    # simliar_actions = Action.objects.filter(user_id=user.id, verb=verb, add_time__get=last_miunte)
    simliar_actions = Action.objects.filter(user_id=user.id, verb=verb)
    
    # 做一个判断，如果传来的要创建的目标是合法的，并且之前这个事物没有被创项目，就新创建这个项目
    # 这里保留一个问题就是add_time__get,这里的__get有什么作用，是截止时间的意思吗？
    # 个人觉得在这里，没必要设置这样一个参数，我们就直接取出当前数据库里面的内容，还是说如果我们在存储过程中，另一个用户创建了这个项目该怎么处理呢
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        saved_actions = simliar_actions.filter(target_ct=target_ct, target_id=target.id)
        
        if not saved_actions:
            action = Action(user=user, verb=verb, target=target)
            action.save()
            return True
    
    return False