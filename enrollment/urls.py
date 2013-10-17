from django.conf.urls.defaults import *
    
urlpatterns = patterns('pycon.enrollment.views',               
    (r'^enroll/$', 'enroll'),
)