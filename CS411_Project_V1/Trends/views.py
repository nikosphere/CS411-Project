from django.template.defaultfilters import title
from pytrends.request import TrendReq
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Trends, catParams, trendParams
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, RestaurantForm, TrendForm
import requests
import json


def finalPy(word):
    trendData = []
    pytrends = TrendReq(hl='en-US', tz=360)  # calls pyTrends
    kw_list = [word]  # calls form from forms.py for user input from HTML file
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='US', gprop='')
    req = pytrends.related_queries()
    req2 = req[word]
    #trendyboiData = {}
    rising1 = req2["rising"]["query"][0]
    rising2 = req2["rising"]["query"][1]
    top1 = req2['top']['query'][0]
    top2 = req2['top']['query'][1]
    top3 = req2['top']['query'][2]
    #trendyboiData['rising1'] = req2["rising"]["query"][0]  # takes the #1 rising from query
    #trendyboiData['top1'] = req2['top']['query'][0]
    #trendData.append(trendyboiData)
    return rising1,rising2,top1,top2,top3


def pytrends_query(request):
    if request.method == 'POST':
        pyt = request.POST['trends']
        pytResult = finalPy(pyt)
        print(pytResult[0])
        print(pytResult[1])
        return render(request, 'Trends/trendy.html',{'pytResult':pytResult},)
    else:
        contextEmpty = {}
        return render(request, 'Trends/trendy.html', contextEmpty)


# def pytrends_query(request):
#     if request.method == 'POST':
#         form = TrendForm(request.POST)
#         form.save()
#     form = TrendForm()
#     trendData = []
#     all_trends = trendParams.objects.all()
#
#     pytrends = TrendReq(hl='en-US', tz=360)  # calls pyTrends
#     kw_list = [all_trends]  # calls form from forms.py for user input from HTML file
#     pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='US', gprop='')  # builds payload for request
#
#     req = pytrends.related_queries() #calls related queries based on input
#     req2 = req[all_trends]
#     print(req)
#     print(req2)
#     trendyboiData = {}
#     trendyboiData['rising1'] = req2["rising"]["query"][0] #takes the #1 rising from query
#     trendyboiData['top1'] = req2['top']['query'][0]
#     trendData.append(trendyboiData)
#     context = {'pyTrendsData': trendData, 'form': form}
#     return render(request, 'Trends/trendy.html',context)  # IMPORTANT ADD IN NEW PAGE OR GO INTO EXISTING MAIN TREND PAGE FOR SEARCH, maybe have it in the search bar?

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
        #form = RestaurantForm(request.POST)
        #form.save()
        #if form.is_valid():
        #    new_search = form.cleaned_data['name']
        #    existing_search_count = catParams.objects.filter(name=new_search).count()
        #    if existing_search_count == 0:
        #        form.save()
        #    else:
        #        err_msg = 'Search is already in database!'

    #form = RestaurantForm()

    #names = catParams.objects.all()
    names=[form]
    restaurant_data = []
    for name in names:
        headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
        params = {'term': name, 'location': 'Boston'}
        req = requests.get(YELP_SEARCH, headers=headers, params=params)
        parsedData = []
        jsonList = json.loads(req.text)
        print(jsonList)
        businesses = jsonList["businesses"]
        for yelp in businesses:
            yelpData = {}
            yelpData['name'] = yelp["name"]
            yelpData['location'] = yelp["location"]["display_address"][0]
            yelpData['rating'] = yelp["rating"]
            yelpData['phone'] = yelp["phone"]
            parsedData.append(yelpData)
            context = {'restaurant_data' : parsedData, 'form':form}
     #   restaurant_data.append(parsedData)
    #context = {'restaurant_data' : restaurant_data, 'form':form}
    return render(request,'Trends/yelp.html', context)


class IndexView(generic.ListView):
    template_name = 'Trends/Index.html'
    context_object_name = 'all_favorites'
    def get_queryset(self):
        return Trends.objects.all()

class DetailView(generic.DetailView):
    model = Trends
    template_name = 'Trends/detail.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'Trends/registration_form.html'

    #display blank form, when a new user comes into the site
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process form data into databse

    def post(self, request):
        form = self.form_class(request.POST or None)

        if form.is_valid():

            user = form.save(commit=False)

            #clean, normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Trends:trends')

        return render(request, self.template_name, {'form': form})