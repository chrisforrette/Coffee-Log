from django.db import models
from django.contrib.auth.models import User
from coffee_log.settings_local import STATUS_OPTIONS

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return str(self.user.username) + "'s profile"