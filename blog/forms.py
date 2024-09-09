from django import forms
from .models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['text', 'photo']  
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email' ,'password1', 'password2')
        