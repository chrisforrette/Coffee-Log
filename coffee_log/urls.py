import os
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    # Static path
    
    (r'^/?(?P<path>(_lib|_img)/.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'http').replace('\\', '/')}),
    
    (r'^/?$', 'coffee_log.coffee.views.index')
    
)
