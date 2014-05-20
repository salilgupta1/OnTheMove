from django.conf.urls import patterns, include, url
from django.contrib import admin
from Onthemove import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Onthemove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home_page, name='home'),
    url(r'^activities/',include('Activities.urls',namespace='Activities')),
    url(r'^users/',include('Users.urls',namespace='Users')),
)
