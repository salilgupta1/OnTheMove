from django.conf.urls import patterns, include, url
from django.contrib import admin
from Activities import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Onthemove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^details(?P<activity_id>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$',views.details, name='details'),
)
