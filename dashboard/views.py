from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Budget, Person, PerPersonMeal, DailySpend
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView 
)
from .forms import NewBudgetForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from PIL import Image
import os

class BudgetView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'dashboard/index.html'
