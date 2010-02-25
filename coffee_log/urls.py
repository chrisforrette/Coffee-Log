import os
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    # Static path
    
    (r'^/?(?P<path>(_lib|_img)/.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'http').replace('\\', '/')}),
    
    # Coffee logs
    
    url(r'^/?$', 'coffee_log.coffee.views.index', name='home'),
    url(r'^coffee-log/add/?$', 'coffee_log.coffee.views.coffee_log_add', name='coffee-log-add'),
    
    # Coffee Places
    
    url(r'^places/?$', 'coffee_log.coffee.views.places', name='coffee-places'),
    url(r'^places/add/?$', 'coffee_log.coffee.views.places_add', name='coffee-places-add'),
    url(r'^places/place/([-_\w]+)/?$', 'coffee_log.coffee.views.place', name='coffee-place'),
    
    # Coffee Roasters
    
    url(r'^roasters/?$', 'coffee_log.coffee.views.roasters', name='coffee-roasters'),
    url(r'^roasters/add/?$', 'coffee_log.coffee.views.roasters_add', name='coffee-roasters-add'),
    url(r'^roasters/([-_\w]+)/?$', 'coffee_log.coffee.views.roaster', name='coffee-roaster'),
    
    # Coffee Beans
    
    url(r'^beans/?$', 'coffee_log.coffee.views.beans', name='coffee-beans'),
    url(r'^beans/add/?$', 'coffee_log.coffee.views.beans_add', name='coffee-beans-add'),
    url(r'^beans/([-_\w]+)/?$', 'coffee_log.coffee.views.bean', name='coffee-bean'),
    
    # Search
    
    url(r'^search/(places|roasters|beans)/?$', 'coffee_log.coffee.views.search_autocomplete', name='search'),
    
    # Users
    
    url(r'^users/?$', 'coffee_log.users.views.index', name='users'),
    url(r'^users/login/?$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}, name='users-login'),
    (r'^users/logout/?$', 'coffee_log.users.views.logout_view'),
    url(r'^users/register/?$', 'coffee_log.users.views.register', name='users-register'),
    (r'^users/send-confirmation/(\d+)/?$', 'coffee_log.users.views.send_confirmation'),
    (r'^users/confirm/([a-z0-9]+)/?$', 'coffee_log.users.views.confirm'),
    (r'^users/([-_\w]+)/?$', 'coffee_log.users.views.profile'),
    
    
)
