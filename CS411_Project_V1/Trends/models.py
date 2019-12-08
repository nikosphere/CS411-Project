from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class catParams(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'names'
class trendParams(models.Model):
    trends = models.CharField(max_length=45)

    def __str__(self):
        return self.trends

class favorites(models.Model):
    favorite_places = models.ManyToManyField(catParams, related_name= "favorite_places", blank=True)

# creates the Trends class which will be used to store the information within our database
class Trends(models.Model):
    trendSearch = models.CharField(max_length=250)
    trendCategory = models.CharField(max_length=250)
    trendLocation = models.CharField(max_length=500)

    # define a string representation of the object from the database
    # specify what we want it to print out
    def __str__(self):
        return self.trendCategory + ' - ' + self.trendSearch + ' - ' + self.trendLocation

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    interest1 = models.CharField(max_length=50, default='')
    interest2 = models.CharField(max_length=50, default='')
    interest3 = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.user.username
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
# foreign key is used when something is part of something else
# you give the key and then it returns what you want

# on_delete.Cascade --> whenever you delete a Trend, it deletes everything associated
# with it


class YelpSearch(models.Model):
    searchParams = models.ForeignKey(Trends, on_delete=models.CASCADE, default=None, blank=None, null=True)
    yelpLocation = models.CharField(max_length=500, default=None, blank=True, null=True)
    yelpCategory = models.CharField(max_length=250, default=None, blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.yelpCategory
