import math
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from coffee_log.coffee.models import *

# Home page

def index(request):
    
    coffee_logs = CoffeeLog.objects.filter(status=2)[:10]
    
    # Get coffee drinks and counts
    
    drinks = CoffeeDrink.objects.filter(status=2).annotate(Count('coffeelog'))
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
    
    places = CoffeePlace.objects.filter(status=2).annotate(Count('coffeelog')).order_by('coffeelog__count')
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
    
    # Count homemade
    
    homemade = CoffeeLog.objects.values('is_homemade').filter(status=2).annotate(count=Count('pk'))
    homemade_names = ['Homemade', 'Not Homemade']
    homemade_counts = {}
    homemade_pcts = []
    
    for count in homemade:
        if count['is_homemade'] == 1:
            homemade_counts[0] = count['count']
        else:
            homemade_counts[1] = count['count']
    
    homemade_counts = list(homemade_counts.values())
    total = sum(homemade_counts)
    
    for count in homemade_counts:
        homemade_pcts.append(int(round((float(count)/float(total)) * 100)))
    
    # ---- Hot spots
    
    # Most visited
    
    time = ''
    
    places_most_visited = CoffeePlace.objects.all().annotate(Count('coffeelog')).order_by('-coffeelog__count')[0:5]
    
    # Newest spots
    
    places_new = CoffeePlace.objects.all().annotate(Count('coffeelog')).order_by('-created')[0:5]
    
    return render_to_response('coffee/index.html', locals())

@login_required
def coffee_log_add(request):
        
    from coffee_log.coffee.forms import CoffeeLogAddForm
    
    if request.method == 'POST':
        data = request.POST.copy()
        data['user'] = int(request.user.pk)
        form = CoffeeLogAddForm(data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CoffeeLogAddForm()
    
    print request.user.pk
    print type(form)
    
    return render_to_response('coffee/coffee_log_add.html', locals())

# Coffee places list

def places(request):
    from django.core.paginator import Paginator
    current_page = request.GET.get('p', 1)
    paginator = Paginator(CoffeePlace.objects.filter(status=2).annotate(Count('coffeelog')), 5)
    
    if (int(current_page) > paginator.num_pages or int(current_page) < 1):
        current_page = 1
    
    paginate = paginator.page(current_page)
    return render_to_response('coffee/places.html', locals())

# Coffee place add

def places_add(request):
    
    from coffee_log.coffee.forms import CoffeePlaceAddForm
    
    if request.method == 'POST':
        form = CoffeePlaceAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/places/')
    else:
        form = CoffeePlaceAddForm()
    
    return render_to_response('coffee/places_add.html', locals())

# Coffee place page

def place(request, slug):
    coffee_place = get_object_or_404(CoffeePlace, slug=slug)
    
    # Coffee logs
    
    coffee_logs = CoffeeLog.objects.filter(coffee_place=coffee_place)[:10]
    
    return render_to_response('coffee/place.html', locals())

# Coffee roasters list

def roasters(request):
    coffee_roasters = CoffeeRoaster.objects.filter(status=2)
    return render_to_response('coffee/roasters_index.html', locals())

# Coffee roasters list

def roasters_add(request):
    
    from coffee_log.coffee.forms import CoffeeRoasterAddForm
    
    if request.method == 'POST':
        form = CoffeeRoasterAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/roasters/')
    else:
        form = CoffeeRoasterAddForm()
    
    return render_to_response('coffee/roasters_add.html', locals())

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

# Coffee beans add

def beans_add(request):

    from coffee_log.coffee.forms import CoffeeBeanAddForm

    if request.method == 'POST':
        form = CoffeeBeanAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/beans/')
    else:
        form = CoffeeBeanAddForm()
    
    return render_to_response('coffee/beans_add.html', locals())

# Search

def search_autocomplete(request, which):
    
    from django.utils.encoding import smart_str
    
    limit = request.GET.get('limit', 10)
    query = smart_str(request.GET.get('q', None))
    
    results = ''
    rows = []
    
    if query:
        if which == 'places':
            rows = CoffeePlace.objects.filter(
                Q(name__icontains=query) 
                | Q(address__icontains=query)
                | Q(city__icontains=query)
            ).order_by('name')[:limit]
        elif which == 'roasters':
            rows = CoffeeRoaster.objects.filter(Q(name__icontains=query)).order_by('name')[:limit]
        elif which == 'beans':
            rows = CoffeeBean.search.query(query)
            # rows = CoffeeBean.objects.filter(name__icontains=query) 

        if rows:
            for row in rows:
                results += '%d|%s\n' % (row.pk, row.name)
    
    # return render_to_response('autocomplete.html', locals())
    return HttpResponse(results)