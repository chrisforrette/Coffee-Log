import os
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    # Static path
    
    (r'^/?(?P<path>(_lib|_img)/.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'http').replace('\\', '/')}),
    
    # Coffee logs
    
    (r'^/?$', 'coffee_log.coffee.views.index'),
    (r'^coffee-log/add/?$', 'coffee_log.coffee.views.coffee_log_add'),
    
    # Coffee Places
    
    (r'^places/?$', 'coffee_log.coffee.views.places'),
    (r'^places/([-_\w]+)/?$', 'coffee_log.coffee.views.place'),
    
    # Coffee Roasters
    
    (r'^roasters/?$', 'coffee_log.coffee.views.roasters'),
    (r'^roasters/([-_\w]+)/?$', 'coffee_log.coffee.views.roaster'),
    
    # Coffee beans
    
    (r'^beans/?$', 'coffee_log.coffee.views.beans'),
    (r'^beans/([-_\w]+)/?$', 'coffee_log.coffee.views.bean'),
    
    # Users
    
    (r'^users/login/?$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    (r'^users/logout/?$', 'coffee_log.users.views.logout_view'),
    (r'^users/register/?$', 'coffee_log.users.views.register'),
    (r'^users/send-confirmation/(\d+)/?$', 'coffee_log.users.views.send_confirmation'),
    (r'^users/confirm/([a-z0-9]+)/?$', 'coffee_log.users.views.confirm'),
    
    
)
