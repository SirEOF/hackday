# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from datetime import date

class UserInfo(models.Model):
    '''用户信息'''
    user = models.ForeignKey(User)
    nickname = models.CharField(u'昵称', max_length=200)
    score = models.CharField(u'积分', max_length=200, default='0')
    stars = models.CharField(u'评分', max_length=200, default='0.0')
    visit = models.CharField(u'访问量', max_length=200, default='0')
    age = models.CharField(u'年龄', max_length=200, default='未知')
    location = models.CharField(u'所在地', max_length=200, default='未知')
    motto = models.TextField(u'座右铭', default='我很懒，什么都不想写')
    avatar = models.URLField(u'头像', default='img/default_avatar.png')
    other = models.CharField(u'推荐对象', max_length=200, blank=True)
    date = models.DateField(u'更新日期', default=date(1970,1,1))
