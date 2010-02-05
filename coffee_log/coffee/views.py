import math
from django.shortcuts import render_to_response, get_object_or_404
from coffee_log.coffee.models import CoffeeLog, CoffeeDrink

def index(request):
    coffee_logs = CoffeeLog.objects.all()
    coffee_drinks = CoffeeDrink.objects.all()
    
    drink_names = []
    drink_counts = []
    drink_pcts = []
    total = 0
    
    for drink in coffee_drinks:
        count = CoffeeLog.objects.filter(coffee_drink=drink.pk).count()
        drink_names.append(drink)
        drink_counts.append(count)
        total += count
    
    # Figure percents
    
    for count in drink_counts:
        drink_pcts.append(int(round((float(count)/float(total)) * 100)))
    
    return render_to_response('coffee/index.html', locals())