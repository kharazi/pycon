from django.conf.urls.defaults import *
    
urlpatterns = patterns('pycon.conference.views',               
    (r'^talk/submit/$', 'SubmitTalk'),
    (r'^talk/update/$', 'UpdateTalk'),  
    (r'^talk/status/$', 'StatusTalk'),  
    (r'^talk/accepted/$', 'AcceptedTalk'),      
)