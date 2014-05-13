from django.conf.urls import patterns, include, url
from django.contrib import admin
from Activities import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Onthemove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),create_Activity,name='create_activity'
    url(r'^details/$',views.details, name='details'),
    url(r'^create_activity/$',views.create_Activity,name='create_Activity'),
)
