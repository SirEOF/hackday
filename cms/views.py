# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.forms import *

from cms.forms import *
from cms.models import *
from account.views import *

def Home(request):
    '''主页'''
    if request.user.is_authenticated():
        user = request.user
        userinfo = user.userinfo_set.all()[0]
    title = u'主页'
    position = 'home'
    return render_to_response('home.html', locals())

def Post(request):  
    '''编辑博文和处理'''
    if request.user.is_authenticated():
        user = request.user
        userinfo = user.userinfo_set.all()[0]
    else:
        return HttpResponseRedirect('/login/?Error=LoginFirst&callback=/post/')
    if request.method == 'POST':
        form = TestUEditorForm(request.POST) 
        if form.is_valid():
            blog = Blog(uid=str(len(Blog.objects.all())+1).zfill(4), title=request.POST['title'], content=request.POST['content'])   
            blog.user = user 
            blog.save()
            return HttpResponseRedirect('/timeline/')
    else:
        form = TestUEditorForm() 
    title = u'新的博文'
    position = 'post'
    return render_to_response('post.html', locals())

def TimeLine(request):
    '''时间轴'''
    if request.user.is_authenticated():
        user = request.user
        userinfo = user.userinfo_set.all()[0]
    else:
        return HttpResponseRedirect('/login/?Error=LoginFirst&callback=/timeline/')
    blogs = Blog.objects.order_by('-time')
    for index, i in enumerate(blogs):
        if index % 2 == 0:
            i.isodd = True
        else:
            i.isodd = False
    title = u'时间轴'
    position = 'timeline'
    count = len(blogs)
    stars_full = range(0, int(float(userinfo.stars)))
    stars_empty = range(0, 5 - int(float(userinfo.stars)))
    return render_to_response('timeline.html', locals())
        
def Detail(request, uid):
    '''博文详细'''
    if request.user.is_authenticated():
        user = request.user
        userinfo = user.userinfo_set.all()[0]
    else:
        return HttpResponseRedirect('/login/?Error=LoginFirst&callback=/timeline/')
    try:
        blog = Blog.objects.get(uid=uid)
    except Blog.DoesNotExist:
        raise Http404
    title = blog.title
    position = 'detail'
    return render_to_response('detail.html', locals())


