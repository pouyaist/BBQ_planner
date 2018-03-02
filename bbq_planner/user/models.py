from django.db import models
from django.contrib.auth.models import User
from food.models import FoodOrder


class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, blank = True)
    is_admin = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, default = None, blank = True)

    class Meta:
        db_table = 'user_profiles'


class Attendee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank = True)
    last_name = models.CharField(max_length=50, blank = True)
    number_of_guests = models.IntegerField(default=0)
    food_orders = models.ManyToManyField(FoodOrder)

    class Meta:
        db_table = 'attendees'
