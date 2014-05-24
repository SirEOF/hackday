# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cms.views.Home', name='home'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^post/', 'cms.views.Post', name='post'),
    url(r'^timeline/', 'cms.views.TimeLine', name='timeline'),
    url(r'^detail/(.+)/$', 'cms.views.Detail', name='detail'),
    url(r'^login/', 'account.views.Login', name='login'),
    url(r'^logout/', 'account.views.Logout', name='logout'),
    url(r'^register/', 'account.views.Register', name='register'),
    url(r'^account/', 'account.views.UserCenter', name='account'), 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
