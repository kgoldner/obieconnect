from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from bootstrap.views import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    #Registration
    (r'^accounts/', include('registration.urls')),
    
    (r'^$', home),
    (r'^inside/$', inside),
    
    (r'^directory', directory),
    
    (r'^directory', directory),   
    
    #Ajax Form
    (r'^ajax_form', ajax_form),
    (r'^ajax_example', ajax_example),
    
    #modal dialog
    (r'^modal_dialog/$', modal_dialog),
    (r'^text_modal_dialog/$', text_modal_dialog),
    
    #ajax autocomplete
    (r'^ajax_autocomplete/$', ajax_autocomplete),
    (r'^ajax_autocomplete_lookup/$', ajax_autocomplete_lookup),
    (r'^ajax_autocomplete_get_selected_item/$', ajax_autocomplete_get_selected_item),
    
    #Popovers
    (r'^popover/$', popover),
    
    #Geolocation
    (r'^geolocation/$', geolocation),    
    
    #Humans and Robots
    ('^humans.txt$', direct_to_template, {'template':'humans.txt', 'mimetype':'text/plain'}),
    ('^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
)
