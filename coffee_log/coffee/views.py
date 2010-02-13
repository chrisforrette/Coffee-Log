import math
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from coffee_log.coffee.models import *

# Home page

def index(request):
    
    coffee_logs = CoffeeLog.objects.all()[:10]
    
    # Get coffee drinks and counts
    
    drinks = CoffeeDrink.objects.all().annotate(Count('coffeelog'))
    drink_names = []
    drink_counts = []
    drink_pcts = []
    
    for drink in drinks:
        if drink.coffeelog__count > 0:
            drink_names.append(drink.name)
            drink_counts.append(drink.coffeelog__count)
    
    total = sum(drink_counts)
    
    # Figure percents
    
    for count in drink_counts:
        drink_pcts.append(int(round((float(count)/float(total)) * 100)))
    
    # Count place visits
    
    places = CoffeePlace.objects.all().annotate(Count('coffeelog'))
    place_names = []
    place_counts = []
    place_pcts = []
    
    for place in places:
        if place.coffeelog__count > 0:
            place_names.append(place.name)
            place_counts.append(place.coffeelog__count)
    
    total = sum(place_counts)
    
    for count in place_counts:
        place_pcts.append(int(round((float(count)/float(total)) * 100))) 
    
    return render_to_response('coffee/index.html', locals())

@login_required
def coffee_log_add(request):
    
    from coffee_log.coffee.forms import CoffeeLogAddForm
    
    if request.method == 'POST':
        form = CoffeeLogAddForm(request.POST)
        
    else:
        form = CoffeeLogAddForm()
    
    return render_to_response('coffee/coffee_log_add.html', locals())

# Coffee places list

def places(request):
    coffee_places = CoffeePlace.objects.filter(status=2)
    return render_to_response('coffee/places.html', locals())

# Coffee place page

def place(request, slug):
    coffee_place = get_object_or_404(CoffeePlace, slug=slug)
    
    # Coffee logs
    
    coffee_logs = CoffeeLog.objects.filter(coffee_place=coffee_place)[:10]
    
    return render_to_response('coffee/place.html', locals())

# Coffee roasters list

def roasters(request):
    coffee_roasters = CoffeeRoaster.objects.filter(status=2)
    return render_to_response('coffee/roasters.html', locals())

# Coffee roaster page

def roaster(request, slug):
    coffee_roaster = get_object_or_404(CoffeeRoaster, slug=slug)

    # Coffee beans

    coffee_beans = CoffeeBean.objects.filter(roaster=coffee_roaster)

    # Coffee Places
    
    coffee_places = CoffeePlace.objects.filter(roaster=coffee_roaster)

    return render_to_response('coffee/roaster.html', locals())

# Coffee beans list

def beans(request):
    coffee_beans = CoffeeBean.objects.filter(status=2)
    return render_to_response('coffee/beans.html', locals())

# Coffee bean page

def bean(request, slug):
    coffee_bean = get_object_or_404(CoffeeBean, slug=slug)

    # Coffee logs

    coffee_logs = CoffeeLog.objects.filter(coffee_bean=coffee_bean)[:10]

    return render_to_response('coffee/bean.html', locals())