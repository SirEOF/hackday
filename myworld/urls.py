from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'cms.testview.home', name='home'),
    url(r'^login/$', 'cms.testview.login', name='login'),
    url(r'^register/$', 'cms.testview.register', name='register'),
    url(r'^timeline/$', 'cms.testview.timeline', name='timeline'),
    url(r'^detail/(?P<id>[0-9]+)', 'cms.testview.detail', name='detail'),
)
