from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os
from django.utils import timezone
from user.models import Profile

class Person(models.Model):
  name = models.CharField(max_length=30)
  deposite = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  balance = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  
  def __str__(self):
    return self.name

class PerPersonMeal(models.Model):
  person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=30, default=person.name)
  total_meals = models.IntegerField(default=0, null=True)
  
  def __str__(self):
    return self.name
  
  
class DailySpend(models.Model):
  date = models.DateField(default=timezone.now)
  meal = models.ManyToManyField(PerPersonMeal)
  total_daily_meals = models.DecimalField(max_digits=2, decimal_places=1, default=(0.0), null=True)
  
  def __str__(self):
    return self.date.strftime("%m/%d/%Y")
  
  

class Budget(models.Model):
  name = models.CharField(max_length=30, null=True)
  total_members = models.IntegerField(default=1)
  start_date = models.DateTimeField(default=timezone.now)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  members = models.ManyToManyField(Person)
  
  editors = models.ManyToManyField(Profile)
  
  total_budget = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  food_budget = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  house_rent = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  elec_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  gas_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  water_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  other_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  
  def __str__(self):
    return self.name
  
#  absolute URL


  
  