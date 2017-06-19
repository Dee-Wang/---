# -*- coding: utf-8 -*-
__author__ = 'Dee'
__date__ = '17-6-19 下午4:39'

from django.core.mail import send_mail

from random import Random

from user.models import EmailVerifyRecord
from chihuoapp.settings import DEFAULT_FROM_EMAIL


def general_random_str(randomlength):
    str = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_email(email, send_type):
    email_record = EmailVerifyRecord()
    # 当验证码用于用户登陆后重置邮箱的时候，发送的验证码是4位的，其他情况下验证码是16位的
    if send_type == "change_email":
        code = general_random_str(4)
    else:
        code = general_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "Food Share注册激活链接"
        email_body = "请点击下面的链接激活你的账户：http://127.0.0.1:8000/user/active_user/{0}".format(code)

    elif send_type == "forget_password":
        email_title = "Food Share密码重置链接"
        email_body = "请点击下面的链接重置密码：http://127.0.0.1:8000/user/reset_pwd/{0}".format(code)

    elif send_type == "change_email":
        email_title = "Food Share修改邮箱验证码"
        email_body = "这是您的验证码：{0}".format(code)

    send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
    if send_status:
        pass