from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import os
from django.utils import timezone
from user.models import Profile


class DailySpend(models.Model):
  date = models.DateField(default=timezone.now)
  amount_Spent = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True)
  
  def __str__(self):
    return self.date.strftime("%m/%d/%Y")
  
  

class Budget(models.Model):
  name = models.CharField(max_length=30, null=True)
  start_date = models.DateTimeField(default=timezone.now)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  
  total_budget = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  food_budget = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  house_rent = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  elec_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  gas_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  water_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  other_bill = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  balance = models.DecimalField(max_digits=20, decimal_places=2, default=(0.00), null=True, blank=True)
  
  def __str__(self):
    return self.name
  
#  absolute URL


  
  