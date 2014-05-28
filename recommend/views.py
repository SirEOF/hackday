# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from time import time
from datetime import date

from account.models import UserInfo
from cms.models import Blog

def matcher(user):
    userinfo = user.userinfo_set.all()[0]
    if not (date.today() == userinfo.date):
        userinfo.date = date.today()
        userinfo.other = str(int(time()) % len(User.objects.all()) + 1)
        userinfo.save()
        if int(userinfo.other)==int(user.id):
            userinfo.other = str(int(userinfo.other) % len(User.objects.all()) + 1)
        userinfo.save()
        return True

def TimeLine(request):
    '''对方的时间轴'''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    user = request.user
    a = matcher(user)
    userinfo = user.userinfo_set.all()[0]
    other = User.objects.get(id=int(userinfo.other))   
    otherinfo = other.userinfo_set.all()[0]
    blogs = other.blog_set.all()
    title = otherinfo.nickname + u'的时间轴'
    position = 'others_timeline'
    count = len(blogs)
    return render_to_response('others_timeline.html', locals())

def Detail(request, uid):
    '''对方的博文详细'''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    user = request.user
    userinfo = user.userinfo_set.all()[0]
    matcher(user)
    other = User.objects.get(id=int(userinfo.other))   
    otherinfo = other.userinfo_set.all()[0]
    try_blog = other.blog_set.filter(uid=uid)
    if try_blog:
        blog = try_blog[0]
    else:
        return HttpResponseRedirect('/')
    title = blog.title 			
    position = 'others_detail'
    return render_to_response('detail.html', locals())
    
        
    
    
