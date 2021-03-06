from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from coffee_log.settings import SECRET_KEY
from coffee_log.coffee.models import CoffeeLog
from coffee_log.users.models import *
from coffee_log.users.forms import UserRegistrationForm

def index(request):
    users = User.objects.filter(is_active=True).annotate(Count('coffeelog')).order_by('-coffeelog__created')
    return render_to_response("users/index.html", locals())

def logout_view(request):
    
    """
    Logout user
    """
    
    logout(request)
    return HttpResponseRedirect('/?logout=1')

def register(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.is_active = False
            user.save()
            return HttpResponseRedirect('/users/send-confirmation/%d/' % user.pk)
    else:
        initial = {}
        
        if request.GET:
            if 'email' in request.GET:
                initial['email'] = request.GET['email']
            if 'username' in request.GET:
                initial['username'] = request.GET['username']
        
        form = UserRegistrationForm(initial=initial)
    
    return render_to_response('users/register.html', locals())

def send_confirmation(request, user_id):
    
    from django.template.loader import render_to_string
    from django.core.mail import send_mail
    from django.contrib.auth.models import get_hexdigest
    
    user = User.objects.get(pk=user_id)
    user.userprofile.set_confirmation_hash()
    user.userprofile.save()
    
    confirmation_url = 'http://' + request.META['HTTP_HOST'] + '/users/confirm/%s/' % user.userprofile.confirmation_hash
    
    message = render_to_string('email/send_confirmation.txt', locals())
    send_mail('Coffee Log: Confirm your registration', message, '', [user.email])
    
    return render_to_response('users/send_confirmation.html', locals())

def confirm(request, confirmation_key):
    user_profile = UserProfile.objects.get(confirmation_hash=confirmation_key)
    activated = False
    if user_profile:
        user_profile.user.is_active = True
        user_profile.user.save()
        activated = True
    return render_to_response('users/confirm.html', locals())


def profile(request, username):
    profile_user = get_object_or_404(User, username=username, is_active=1)
    
    coffee_logs = CoffeeLog.objects.filter(status=2, user=profile_user.pk)[:10]
    
    # ---- Stats
    
    # Average per day
    
    avg_logs_per_day = CoffeeLog.objects.get_avg_per_day(profile_user.pk)
    
    # Favorite drink
    
    favorite_drink = CoffeeDrink.objects.filter(status=2, coffeelog__user=profile_user.pk).annotate(count=Count('coffeelog__coffee_drink')).order_by('-count')[:1]
    if favorite_drink:
        favorite_drink = favorite_drink[0]
    
    # Favorite place
    
    favorite_place = CoffeePlace.objects.filter(status=2, coffeelog__user=profile_user.pk).annotate(count=Count('coffeelog__coffee_place')).order_by('-count')[:1]
    if favorite_place:
        favorite_place = favorite_place[0]
    
    # Favorite bean

    favorite_bean = CoffeeBean.objects.filter(status=2, coffeelog__user=profile_user.pk).annotate(count=Count('coffeelog__coffee_bean')).order_by('-count')[:1]
    if favorite_bean:
        favorite_bean = favorite_bean[0]
    
    return render_to_response('users/profile.html', locals())