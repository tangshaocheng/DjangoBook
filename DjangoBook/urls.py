from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('mysite.views',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'hello'),
    url(r'^$', 'my_homepage_view'),
    url(r'^time/$', 'current_time'),
    url(r'^another-time-page$', 'current_time'),
    url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^meta/$', 'all_meta'),
    url(r'^search/$', 'search'),
    url(r'^contact/$', 'contact'),
    url(r'^join/$', 'join'),
    url(r'^joinform/$', 'joinform'),
    url(r'^register/$', 'registerform'),
    url(r'^toregister/$', 'register'),
    url(r'^login/$', 'loginform'),
    url(r'^tologin/$', 'login'),
    url(r'^home/$', 'homeform'),
    url(r'^joindetail/$', 'joindetail'),
)



