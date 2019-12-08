from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'Trends'
urlpatterns = [
    #/trends/
    path('', views.IndexView.as_view(), name='trends'),
    #/trends/favorites
    #will give you a specific place for your favorite
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('yelp/', views.yelp_query, name ='search'),
    path('random/', views.get_random_recipe, name='randomRecipe'),
    path('pyTrends/', views.pytrends_query, name = 'pyTrendsRes'),
    #custom registration for a user
    path('login/', LoginView.as_view(template_name='trends/user_login.html'), name ='login'),
    #logout of manual user
    path('logout/', LogoutView.as_view(template_name='trends/logout.html'),name = 'logout'),
    #
    #new user registration
    path('register/',views.register, name ='register'),
    #create profile page
    path('profile/',views.view_profile, name='profile'),
    #edit your account
    path('edit/', views.edit_profile, name = 'edit_profile'),
    #change the password of your account
    path('change-password', views.change_password, name='change_password'),
    #change password through email
    # login via fb
    path("join/", views.login, name='join'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    # path("", views.home, name="home"),
]
