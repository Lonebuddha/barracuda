from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barracuda.views.home', name='home'),
    # url(r'^barracuda/', include('barracuda.foo.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    
    url(r'^admin/', include(admin.site.urls)),
)
