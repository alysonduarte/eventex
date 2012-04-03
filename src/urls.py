
from django.conf.urls.defaults import patterns, include
#from django.contrib import admin
#admin.autodiscover()



urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
    (r'^inscricao/', include('subscriptions.urls', namespace='subscriptions')),
    
#   (r'^admin/', include(admin.site.urls)),

)


'''from django.conf.urls.defaults import patterns, include, url
from core.views import homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.homepage'),
    url(r'^inscricao/', include ('subscriptions.urls', namespace ='subscriptions')),
)   
#urlpatterns += staticfiles_urlpatterns()
'''