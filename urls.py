from obieconnect.views import *
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',                  
    url(r'^$', main_page),
    
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    
    url(r'^dept/([-\w]+)/$', dept_info),
    url(r'^prof/([-\w]+)/$', prof_info),
)
