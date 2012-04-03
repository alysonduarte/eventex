from django.conf.urls.defaults import patterns, url
from django.conf.urls.defaults import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('subscriptions.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)