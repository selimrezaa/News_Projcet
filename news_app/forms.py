from django.forms import ModelForm
from django import forms
from news_app.models import *
from django.contrib.auth.forms import UserCreationForm


class AddNews(forms.ModelForm):
    
    class Meta:
        model = News
        fields = '__all__'

class CreateNewUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'username',  'password1', 'password2')