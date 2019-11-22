from pytrends.request import TrendReq
from django.views import generic
from .models import Trends, catParams
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, RestaurantForm
import requests
import json

#pytrends = TrendReq(hl='en-US', tz=360)
#kw_list = ["Boston North End"]
#pytrends.build_payload(kw_list, cat=188, timeframe='today 1-m', geo='US-MA', gprop='')
#stuff = pytrends.interest_over_time()
#print(stuff)

def login(request):
    return render(request, 'Trends/join.html')

@login_required
def home(request):
    return render(request, 'Trends/home.html')

@login_required
def yelp_query(request):
    business_id = '_b_RUDVdh3IY_pNDXn2rPw'
    YELP_API_KEY = '4F_2Zz_KqR8W9sQGdEOr3W8kvMLHrHhjmZwaIIKWnz95thdXigFNVa6LTd7QZ0mOf8gAb4IGX_bKa-_qPBWeIW__-gTFhCdRUbwZu-jWNzTqI5PBdlI41U2W9KSvXXYx'
    YELP_SEARCH = 'https://api.yelp.com/v3/businesses/search'.format(business_id)

    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        form.save()

    form = RestaurantForm()

    names = catParams.objects.all()
    restaurant_data = []
    for name in names:
        headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
        params = {'term': name, 'location': 'Boston'}
        req = requests.get(YELP_SEARCH, headers=headers, params=params)
        parsedData = []
        jsonList = json.loads(req.text)
        businesses = jsonList["businesses"]
        for yelp in  businesses:
            yelpData = {}
            yelpData['name'] = yelp["name"]
            yelpData['location'] = yelp["location"]["display_address"]
            yelpData['rating'] = yelp["rating"]
            yelpData['phone'] = yelp["phone"]
            parsedData.append(yelpData)
        restaurant_data.append(parsedData)
    context = {'restaurant_data' : restaurant_data, 'form':form}
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