from django.conf.urls import patterns, include, url
from django.contrib import admin
from Users import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^create_user/$',views.create_user,name='create_user'),
)