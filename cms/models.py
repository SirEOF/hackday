# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from DjangoUeditor.models import UEditorField

class Blog(models.Model):
    '''博文内容'''
    user = models.ForeignKey(User)
    private = models.BooleanField(u'是否为私密', default=False)
    uid = models.CharField(u'博文编号', max_length=10)
    title = models.CharField(u'题目', max_length=100)
    content = models.TextField()
    time = models.DateTimeField(u'评论时间', auto_now_add=True)
    

