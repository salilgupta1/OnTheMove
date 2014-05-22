from django.conf.urls import patterns, include, url
from django.contrib import admin
from Users import views
from forms import OnthemoveUserLoginForm
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^create_user/$',views.create_user,name='create_user'),
    url(r'^login/$','django.contrib.auth.views.login',
        {'template_name':'Users/login.html',
        'authentication_form':OnthemoveUserLoginForm},
        name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',
        {'next_page':'/'},
        name='logout'),
    url(r'^my_activities/$',views.my_activity,name='my_activities'),
    url(r'^my_participants/(?P<act_id>\d+)/$',views.my_participants,name='my_participants')
)