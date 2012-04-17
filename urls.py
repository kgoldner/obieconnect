from obieconnect.views import *
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',                  
    url(r'^$', main_page),
    
    url(r'^register/$', register),
    url(r'^login/$', custom_login),
    url(r'^logout/$', logout_page),
    
    url(r'^dept/([-\w]+)/$', dept_info),
    url(r'^prof/([-\w]+)/$', prof_info),
    
    # need url for course page
)
