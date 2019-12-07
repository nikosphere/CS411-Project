from django import forms
from django.conf import settings
from django.contrib.auth.models import User
import requests
from .models import catParams, trendParams
from django.forms import ModelForm, TextInput, Form


class RestaurantForm(ModelForm):
    class Meta:
        model = catParams
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Look-up'})}

class TrendForm(ModelForm):
    #example = forms.CharField(label='trends', widget=forms.TextInput(attrs={'placeholder':'Look-up'}))
    class Meta:
        model = trendParams
        fields = ['trends']
        widget = {'trends': TextInput(attrs={'class': 'form-control', 'placeholder': 'Look Up'})}


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']