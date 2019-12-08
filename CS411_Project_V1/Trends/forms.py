from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields= (
            'username',
            'first_name',
            'last_name',
            'email',
            #'interest1'...
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name =self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )