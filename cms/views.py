# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.forms import *

from cms.forms import *
from cms.models import *
from account.views import *
from recommend.views import matcher

def Home(request):
    '''主页'''
    if request.user.is_authenticated():
        user = request.user
        userinfo = user.userinfo_set.all()[0]
    title = u'主页'
    position = 'home'
    return render_to_response('home.html', locals())

def Post(request, *args):
    '''编辑博文和处理'''
    if request.user.is_authenticated():
        user = request.user
        userinfo = user.userinfo_set.all()[0]
    else:
        return HttpResponseRedirect('/login/?Error=LoginFirst&callback=/post/')
    if request.method == 'POST':
        form = TestUEditorForm(request.POST) 
        if form.is_valid():
            if args: 
                uid = args[0]
                try:
                    blog = Blog.objects.get(uid=uid)
                    blog.title = request.POST['title']
                    blog.content = request.POST['content']
                    blog.private = request.POST.get('private', False)=='on'
                    blog.save()
                except Blog.DoesNotExist:
                    return HttpResponseRedirect('/post/')
            else:
                blog = Blog(uid=str(len(Blog.objects.all())+1).zfill(4), 
                       title=request.POST['title'], 
                       content=request.POST['content'], 
                       private=(request.POST.get('private', False)=='on'))
            blog.user = user 
            blog.save()
            return HttpResponseRedirect('/timeline/')
    else:
        if args: 
            uid = args[0]
            try:
                blog = user.blog_set.get(uid=uid)
                form = TestUEditorForm(initial={'content': blog.content})
            except Blog.DoesNotExist:
                return HttpResponseRedirect('/post/')
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
    blogs = user.blog_set.order_by('-time')
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

    tmp_user = request.user
    tmp_a = matcher(tmp_user)
    tmp_userinfo = tmp_user.userinfo_set.all()[0]
    tmp_other = User.objects.get(id=int(tmp_userinfo.other))
    otherinfo = tmp_other.userinfo_set.all()[0]

    return render_to_response('timeline.html', locals())
        
def Detail(request, uid):
    '''博文详细'''
    if request.user.is_authenticated():
        user = request.user
        userinfo = user.userinfo_set.all()[0]
    else:
        return HttpResponseRedirect('/login/?Error=LoginFirst&callback=/timeline/')
    try_blog = user.blog_set.filter(uid=uid)
    if try_blog:
        blog = try_blog[0]
    else:
        return HttpResponseRedirect('/')
    title = blog.title
    position = 'detail'
    return render_to_response('detail.html', locals())

    


