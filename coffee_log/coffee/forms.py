import datetime
from django import forms
from coffee_log.coffee.models import *

class CoffeeLogAddForm(forms.ModelForm):
    
    # ---- Set options
    
    # Coffee drink options
    
    coffee_drink_opt = CoffeeDrink.objects.filter(status=2).values_list('pk', 'name')
    
    # Coffee drink size options
    
    coffee_drink_size_opt = CoffeeDrinkSize.objects.filter(status=2).values_list('pk', 'name')
    
    # Coffee bean options
    
    coffee_beans = CoffeeBean.objects.filter(status=2)
    coffee_bean_opt = [('', '--- Not Sure ---')]
    
    for bean in coffee_beans:
        coffee_bean_opt.append((bean.pk, unicode(u'%s (%s)' % (bean.name, bean.roaster.name))))
    
    # Coffee place options
    
    coffee_places = CoffeePlace.objects.filter(status=2)
    coffee_place_opt = [('', '--- None ---')]
    
    for place in coffee_places:
        coffee_place_opt.append((place.pk, unicode(u'%s (%s)' % (place.name, place.get_full_address()))))
    
    # ---- Set initial
    
    now = datetime.datetime.now()
    
    # ---- Set fields
    
    consumption_date = forms.DateField(initial=now, error_messages={'required': 'Please enter a date'})
    consumption_time = forms.TimeField(initial=now, error_messages={'required': 'Please enter a time'})
    coffee_bean = forms.IntegerField(widget=forms.Select(choices=tuple(coffee_bean_opt)), required=False)
    coffee_place = forms.IntegerField(widget=forms.Select(choices=tuple(coffee_place_opt)), required=False)
    coffee_drink = forms.IntegerField(widget=forms.Select(choices=tuple(coffee_drink_opt)), error_messages={'required': 'Please select a drink'})
    coffee_drink_size = forms.IntegerField(widget=forms.Select(choices=tuple(coffee_drink_size_opt)), label=u'Drink Size')
        
    class Meta:
        model = CoffeeLog
        fields = (
            'coffee_drink',
            'coffee_drink_size',
            'is_homemade',
            'coffee_bean',
            'coffee_place',
            'notes',
        )
    
    def clean_consumption(self):
        print 'CON'
        return self.consumption