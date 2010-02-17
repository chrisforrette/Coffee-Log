import datetime
from django import forms
from coffee_log.coffee.models import CoffeeLog, CoffeeBean

class CoffeeLogAddForm(forms.ModelForm):
    
    now = datetime.datetime.now()
    consumption_date = forms.DateField(initial=now)
    consumption_time = forms.TimeField(initial=now)
    # coffee_bean_id = forms.IntegerField(widget=forms.HiddenInput)
    # coffee_bean_text = forms.CharField(max_length=255)
        
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