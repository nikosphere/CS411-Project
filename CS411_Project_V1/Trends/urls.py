from django.conf import settings
from django.urls import path, include

from . import views

app_name = 'Trends'
urlpatterns = [
    #/trends/
    path('', views.IndexView.as_view(), name='trends'),
    #/trends/favorites
    #will give you a specific place for your favorite
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('yelp/', views.yelp_query, name ='search'),
    path('trendy/', views.pytrends_query, name = 'trendSearch'),
    path('random/', views.get_random_recipe, name='randomRecipe'),
    path('register', views.UserFormView.as_view(), name ='register'),
    path('register', views.UserFormView.as_view(), name ='register'),
    # login via fb
    path("join/", views.login, name='join'),
    path('logout/', views.logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    # path("", views.home, name="home"),
]
