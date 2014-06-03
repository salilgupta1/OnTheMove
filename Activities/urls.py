from django.conf.urls import patterns, include, url
from django.contrib import admin
from Activities import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Onthemove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^details/(?P<id>\d+)/$',views.details, name='details'),
    url(r'^create_activity/$',views.create_Activity,name='create_Activity'),
    url(r'^addUser/(?P<activity_id>\d+)/(?P<user_id>\d+)$',views.addUser,name='addUser'),
    url(r'^fill_in_yelp/$',views.fill_in_yelp,name='fill_in_yelp')
)

