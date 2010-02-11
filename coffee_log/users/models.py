from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from coffee_log.settings_site import STATUS_OPTIONS

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    confirmation_hash = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=2)
    
    def __unicode__(self):
        return str(self.user.username) + "'s profile"        
    
    def set_confirmation_hash(self):
        self.confirmation_hash = self.generate_confirm_hash()
        return self.confirmation_hash
    
    # Generate confirmation hash based on current week of current year
    
    def generate_confirm_hash(self):
        
        import datetime
        import hashlib
        from coffee_log.settings import SECRET_KEY
        
        # Get current week
        
        year, week, day = datetime.date.today().isocalendar()
        
        # Generate hash
        
        hasher = hashlib.sha1()
        hasher.update(SECRET_KEY)
        hasher.update(str(self.user.pk))
        hasher.update(str(year))
        hasher.update(str(week))
        
        return hasher.hexdigest()

# User post save signal to crate corresponding user profile record

def create_user_profile(sender, instance, signal, *args, **kwargs):
    if 'created' in kwargs and kwargs['created'] == True:
        user_prof = UserProfile(user=instance)
        user_prof.save()

# Signal

models.signals.post_save.connect(create_user_profile, sender=User)