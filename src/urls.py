from django.conf.urls.defaults import patterns, include, url
#from django.conf.urls.defaults import patterns
from core.views import homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),

)
urlpatterns += staticfiles_urlpatterns()
