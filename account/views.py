# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

from myworld.settings import BASE_DIR

from account.models import *

def Login(request):
    '''登入页面和处理'''
    Error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/timeline/')
    if not (request.method == 'POST'):
        if 'callback' in request.GET:
            callback = request.GET['callback']
        title = u'登入'
        position = 'login'
        return render_to_response('login.html', locals())
    else:
        if 'callback' in request.POST:
            callback = request.POST['callback']
        else:
            callback = '/timeline/'
        if not ('email' in request.POST):
            Error = u'邮箱不能为空'
        else:
            if not ('password' in request.POST):
                Error = u'密码不能为空'
    if not Error:
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password']) 
        if user:
            auth.login(request, user)
        else:
	    Error = u'该邮箱未注册或密码错误'
    if Error:
        title = u'登入'
        position = 'login'
        return render_to_response('login.html', {'Error': Error})
    else:
        return HttpResponseRedirect(callback)
            
def Logout(request):
    '''注销'''
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect('/')

def Register(request):
    '''注册页面和处理'''
    if not(request.method == 'POST'):
        if 'callback' in request.GET:
            callback = request.GET['callback']
        title = u'注册'
        position = 'register'
        return render_to_response('register.html', locals())
    Error = u''
    if 'callback' in request.POST:
        callback = request.POST['callback']
    else:
        callback = '/timeline/'
    if not ('email' in request.POST):
        Error = u'邮箱不能为空'
    elif not ('nickname' in request.POST):
        Error = u'昵称不能为空'
    elif not (('password1' in request.POST) and ('password2' in request.POST)):
        Error = u'密码不能为空'
    else:
        try:
            user = User.objects.get(username=request.POST['email'])
            Error = u'该邮箱已注册'
        except User.DoesNotExist:
            if not (request.POST['password1'] == request.POST['password2']):  
                Error = u'两次密码不一致'
            else:
                newuser = User.objects.create_user(username = request.POST['email'], password = request.POST['password1'])
                newuser.save()
                userinfo = UserInfo(nickname=request.POST['nickname'])
                userinfo.user = newuser
                userinfo.save()
                user = auth.authenticate(username = request.POST['email'], password = request.POST['password1']) 
                auth.login(request, user)
    if Error:
        title = u'注册'
        position = 'register'
        return render_to_response('register.html', {'Error': Error})
    else:
        return HttpResponseRedirect(callback)

def UserCenter(request):
    '''用户中心和信息修改'''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    user = request.user
    userinfo = (user.userinfo_set.all())[0]
    if request.method == 'POST':
        userinfo.nickname = (request.POST['nickname'] if request.POST['nickname'] else userinfo.nickname)
        userinfo.age = (request.POST['age'] if request.POST['age'] else userinfo.age)
        userinfo.location = (request.POST['location'] if request.POST['location'] else userinfo.location)
        if auth.authenticate(username=user.username, password=request.POST['old_pwd']) and request.POST['new_pwd1']==request.POST['new_pwd2']:
            user.set_password(request.POST['new_pwd1'])
            user.save()
        if 'avatar' in request.FILES:
            avatar_obj = request.FILES.get('avatar')	
            userinfo.avatar = 'img/avatar' + str(user.id) + '.' + avatar_obj.name.split('.')[1]
            file_obj = open(BASE_DIR + 'static/' + userinfo.avatar, 'wb+')
            file_obj.write(avatar_obj.read())
            file_obj.close()
        userinfo.save()
    title = u'用户中心'
    position = 'account'
    return render_to_response('account.html', locals())          
            
