# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    data = {
        'position': 'home',
        'title': '首页',
    }

    return render_to_response('home.html', data, RequestContext(request))


def login(request):
    data = {
        'position': 'login',
        'title': '登陆',
    }

    return render_to_response('login.html', data, RequestContext(request))


def register(request):
    data = {
        'position': 'register',
        'title': '注册',
    }

    return render_to_response('register.html', data, RequestContext(request))


def timeline(request):
    data = {
        'position': 'timeline',
        'title': '时间轴',
    }

    return render_to_response('timeline.html', data, RequestContext(request))


def detail(request, id):
    data = {
        'position': 'timeline',
        'title': '我的日志',
    }

    return render_to_response('detail.html', data, RequestContext(request))


def post(request, id):
    data = {
        'position': 'post',
        'title': '发表日志',
    }

    return render_to_response('post.html', data, RequestContext(request))