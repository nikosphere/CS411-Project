from django import forms
from django.forms import ModelForm, TextInput
from django.conf import settings
from django.contrib.auth.models import User
import requests
from .models import catParams


from django.forms import ModelForm, TextInput


class RestaurantForm(ModelForm):
    class Meta:
        model = catParams
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Look-up'})}



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class yelpSearch(forms.Form):
    word = forms.CharField(max_length=200)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        endpoint = 'https://api.yelp.com/v3/businesses/{id}'
        url = endpoint.format(source_lang='en', word_id = word)
        headers = {'app_id':settings.YELP_APP_ID, 'app_key':settings.YELP_APP_KEY}
        response = requests.get(url, headers=headers)
        #check if response
        if response.status_code == 200:
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  #not found
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Yelp API is not available at the moment. Please try again later.'
            return result


