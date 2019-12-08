from pytrends.request import TrendReq
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Trends, catParams, trendParams
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm, EditProfileForm
import requests
import json


def finalPy(word):
    pytrends = TrendReq(hl='en-US', tz=360)  # calls pyTrends
    kw_list = [word]  # calls form from forms.py for user input from HTML file
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='US', gprop='')
    req = pytrends.related_queries()
    req2 = req[word]
    rising1 = req2["rising"]["query"][0]
    rising2 = req2["rising"]["query"][1]
    top1 = req2['top']['query'][0]
    top2 = req2['top']['query'][1]
    top3 = req2['top']['query'][2]
    return rising1,rising2,top1,top2,top3


def pytrends_query(request):
    if request.method == 'POST':
        pyt = request.POST['trends']
        pytResult = finalPy(pyt)
        return render(request, 'Trends/Index.html',{'pytResult':pytResult},)
    else:
        contextEmpty = {}
        return render(request, 'Trends/Index.html', contextEmpty)

def pyTrends(request):
    return render(request,'Trends/pyTrends.html')

def login(request):
    return render(request, 'Trends/join.html')

@login_required
def home(request):
    return render(request, 'Trends/yelp.html')

@login_required
def yelp_query(request):
    business_id = '_b_RUDVdh3IY_pNDXn2rPw'
    YELP_API_KEY = '4F_2Zz_KqR8W9sQGdEOr3W8kvMLHrHhjmZwaIIKWnz95thdXigFNVa6LTd7QZ0mOf8gAb4IGX_bKa-_qPBWeIW__-gTFhCdRUbwZu-jWNzTqI5PBdlI41U2W9KSvXXYx'
    YELP_SEARCH = 'https://api.yelp.com/v3/businesses/search'.format(business_id)

    err_msg = ''
    if request.method == 'POST':
        form = request.POST.get('input')
        location = request.POST.get('location')
#need to parse json file for pictures
    names = [form]
    restaurant_data = []
    for name in names:
        headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
        params = {'term': name, 'location': location}
        req = requests.get(YELP_SEARCH, headers=headers, params=params)
        parsedData = []
        jsonList = json.loads(req.text)
        businesses = jsonList["businesses"]
        for yelp in businesses:
            yelpData = {}
            yelpData['name'] = yelp["name"]
            yelpData['location'] = yelp["location"]["display_address"][0]
            yelpData['rating'] = yelp["rating"]
            yelpData['phone'] = yelp["phone"]
            parsedData.append(yelpData)
            context = {'restaurant_data' : parsedData, 'form':form}
    return render(request,'Trends/yelp.html', context)

def get_random_recipe(request):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

    querystring = {"number":"3","tags":"vegetarian%2Cmexican"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "973b1b54f6msh43f13f4453ca65cp1eeee4jsn4696d4dba525"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonList = json.loads(response.text)
    titles = jsonList["recipes"]
    parsedData = []

    for r in titles:
        spoonData = {}
        spoonData['title'] = r['title']
        print(spoonData["title"])
        parsedData.append(spoonData)
        context = {'recipe': parsedData}

    return render(request, 'Trends/spoon.html',context)

class IndexView(generic.ListView):
    template_name = 'Trends/Index.html'
    context_object_name = 'all_favorites'
    def get_queryset(self):
        return Trends.objects.all()

class DetailView(generic.DetailView):
    model = Trends
    template_name = 'Trends/detail.html'

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/trends/trendy')
    else:
        form = RegistrationForm()
        context = {'form':form}
        return render(request, 'Trends/registration.html', context)
def view_profile(request):
    context = {'user':request.user}
    return render(request,'Trends/profile.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/trends/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request,'trends/edit_profile.html', context)

def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(data = request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('trends/edit_profile.html')
        else:
            return redirect('trends/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form':form}
        return render(request,'trends/change_password.html',context)