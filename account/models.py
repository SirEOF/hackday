# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    '''用户信息'''
    user = models.ForeignKey(User)
    nickname = models.CharField(u'昵称', max_length=10)
    score = models.CharField(u'积分', max_length=5, default='0')
    age = models.CharField(u'年龄', max_length=5, default='未知')
    location = models.CharField(u'所在地', max_length=30, default='未知')
    motto = models.CharField(u'座右铭', max_length=100, default='我很懒，什么都不想写')
    
    
    
