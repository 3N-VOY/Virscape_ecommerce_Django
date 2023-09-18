from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(help_text='Your Name')
    last_name = forms.CharField()
    country = forms.CharField()
    address = forms.CharField()
    zipcode = forms.CharField()
    city = forms.CharField()
    
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    # location = forms.CharField(help_text='Put location in here')
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'country', 'address', 
                  'zipcode', 'city',)
        

class EditUserForm(UserChangeForm):
    
    class Meta:
        model = Profile
        fields = ( 'first_name', 'last_name', 'country', 'address', 
                  'zipcode', 'city',)