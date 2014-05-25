# -*- coding: utf-8 -*-

"""
Django settings for myworld project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bcrent^aq5_-%^1@zc)h(oq@va!23ui-dtyxtx&q8p-+o&-3)+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoUeditor',
    'cms',
    'account',
    'album',
    'recommend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'myworld/templates/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

ROOT_URLCONF = 'myworld.urls'

WSGI_APPLICATION = 'myworld.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hackday',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

UEDITOR_SETTINGS={
    "toolbars":{           #定义多个工具栏显示的按钮，允行定义多个
        "name1":[[ 'source', '|','bold', 'italic', 'underline']],
        "name2":[]
    },
    "images_upload":{
        "allow_type":"jpg,png",    #定义允许的上传的图片类型
        "path":"",                   #定义默认的上传路径
        "max_size":"2222kb"        #定义允许上传的图片大小，0代表不限制
    },
    "files_upload":{
        "allow_type":"zip,rar",   #定义允许的上传的文件类型
        "path":"",                  #定义默认的上传路径
        "max_size":"2222kb"       #定义允许上传的文件大小，0代表不限制
    },
    "image_manager":{
        "path":""         #图片管理器的位置,如果没有指定，默认跟图片路径上传一样
    },
    "scrawl_upload":{
        "path":""           #涂鸦图片默认的上传路径
    }
}

