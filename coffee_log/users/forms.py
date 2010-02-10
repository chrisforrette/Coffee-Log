from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    username = forms.RegexField(label='Username', max_length=30, regex=r'^\w+$',
        help_text = "Required. 30 characters or fewer. Alphanumeric characters only (letters, digits and underscores).",
        error_messages = {'invalid': "This value must contain only letters, numbers and underscores" ,'required': 'Please enter a username'})
    email = forms.EmailField(label='Email', error_messages={'required': 'Please enter a valid email address', 'invalid': 'Please enter a valid email address'})
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, error_messages={'required': 'Please enter a password'})
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput, error_messages={'required': 'Please enter a password'})