import math
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Count
from coffee_log.coffee.models import CoffeeLog, CoffeeDrink, CoffeePlace

def index(request):
        
    coffee_logs = CoffeeLog.objects.all()
    coffee_drinks = CoffeeDrink.objects.all()
    
    drink_names = []
    drink_counts = []
    drink_pcts = []
    total = 0
    
    for drink in coffee_drinks:
        count = CoffeeLog.objects.filter(coffee_drink=drink.pk).count()
        if count > 0:
            drink_names.append(drink)
            drink_counts.append(count)
            total += count
    
    # Figure percents
    
    for count in drink_counts:
        drink_pcts.append(int(round((float(count)/float(total)) * 100)))
    
    # Count place visits
    
    places = CoffeePlace.objects.all().annotate(log_count=Count('coffeelog'))
    place_names = []
    place_counts = []
    place_pcts = []
    
    for place in places:
        place_names.append(place.name)
        place_counts.append(place.log_count)
    
    total = sum(place_counts)
    
    for count in place_counts:
        place_pcts.append(int(round((float(count)/float(total)) * 100))) 
    
    return render_to_response('coffee/index.html', locals())

# Coffee places list

def places(request):
    return render_to_response('coffee/places.html', locals())

# Coffee place page

def place(request, slug):
    coffee_place = get_object_or_404(CoffeePlace, slug=slug)
    
    from coffee_log.settings_local import get_geo_point
    
    address = coffee_place.address + ' ' + coffee_place.city + ', ' + coffee_place.state + ' ' + coffee_place.zip
    geo_point = get_geo_point(address)
    geo_point = geo_point[1]
    
    # Coffee logs
    
    coffee_logs = CoffeeLog.objects.filter(coffee_place=coffee_place)[:10]
    
    return render_to_response('coffee/place.html', locals())
