from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf.urls import url

app_name = 'Trends'
urlpatterns = [
    #/trends/
    path('', views.IndexView.as_view(), name='trends'),
    #/trends/favorites
    #will give you a specific place for your favorite
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('yelp/', views.yelp_query, name ='search'),
    path('trendy/', views.pytrends_query, name = 'trendSearch'),
    path('register', views.UserFormView.as_view(), name ='register'),
    path('register', views.UserFormView.as_view(), name ='register'),
    # login via fb
    path("join/", views.login, name='join'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    # path("", views.home, name="home"),
]
