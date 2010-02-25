import time, datetime
from django import forms
from coffee_log.coffee.models import *

class CoffeeLogAddForm(forms.ModelForm):
    
    # ---- Set initial
    
    now = datetime.datetime.now()
    
    # ---- Set fields
    
    consumption = forms.SplitDateTimeField(initial=now, label='Consumption Date/Time')
    coffee_bean = forms.ModelChoiceField(queryset=CoffeeBean.objects.filter(status=2), empty_label='--- Not Sure --', required=False)
    coffee_place = forms.ModelChoiceField(queryset=CoffeePlace.objects.filter(status=2), empty_label='--- N/A ---', required=False)
    coffee_drink = forms.ModelChoiceField(queryset=CoffeeDrink.objects.filter(status=2), empty_label=None, required=True, error_messages={'required': 'Please select a drink'})
    coffee_drink_size = forms.ModelChoiceField(queryset=CoffeeDrinkSize.objects.filter(status=2), empty_label=None, label=u'Drink Size')
        
    class Meta:
        model = CoffeeLog
        fields = (
            'user',
            'coffee_drink',
            'coffee_drink_size',
            'is_homemade',
            'coffee_bean',
            'coffee_place',
            'consumption',
            'notes',
        )

# Coffee place form

class CoffeePlaceAddForm(forms.ModelForm):
    
    class Meta:
        model = CoffeePlace
        exclude = (
            'slug',
            'status'
        )

# Coffee roaster form

class CoffeeRoasterAddForm(forms.ModelForm):

    class Meta:
        model = CoffeeRoaster
        exclude = (
            'slug',
            'status'
        )

# Coffee bean

class CoffeeBeanAddForm(forms.ModelForm):

    class Meta:
        model = CoffeeBean
        exclude = (
            'slug',
            'status'
        )