from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name'] 
        
        
class ProfileUpdateForm(forms.ModelForm):
    image = forms.FileField(required=False)
    image.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Profile
        fields = ['institution',  'location', 'occupation', 'phone', 'bio', 'theme', 'image']
        
        