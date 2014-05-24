# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

import datetime

class UserInfo(models.Model):
    user = models.OneToOneField(User)
    score = models.CharField(u'', max_length=5, default='0')
    name = models.CharField(u'', max_length=10, default='unknown')
    birthday = models.DateField(u'', default=datetime.date(2000,1,1))
    location = models.CharField(u'', max_length=30, default='the earth')
    motto = models.CharField(u'', max_length=100, default='')
    
    
    
