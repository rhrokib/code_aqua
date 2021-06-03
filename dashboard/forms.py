from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile
from .models import Budget
from django.urls import reverse_lazy


class NewBudgetForm(forms.ModelForm):
  class Meta:
    model = Budget
    fields = '__all__'
    