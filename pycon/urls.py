from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from home import views as home_views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pycon.views.home', name='home'),
    # url(r'^pycon/', include('pycon.foo.urls')),
    # url(r'^/$', home_views.home)
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^enrollment/', include('enrollment.urls')),    
    (r'^conference/', include('conference.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

)
