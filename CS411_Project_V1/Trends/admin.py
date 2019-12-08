from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Trends, YelpSearch, catParams, UserProfile

admin.site.register(Trends)
admin.site.register(YelpSearch)
admin.site.register(catParams)
admin.site.register(UserProfile)