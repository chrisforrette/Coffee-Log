from django import forms
from coffee_log.coffee.models import CoffeeLog

class CoffeeLogAddForm(forms.ModelForm):
        
    class Meta:
        model = CoffeeLog
        fields = (
            'coffee_drink',
            'coffee_drink_size',
            'is_homemade',
            'coffee_bean',
            'coffee_place',
            'notes',
            'consumption',
        )