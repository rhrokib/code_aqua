from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Budget, DailySpend
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from PIL import Image
import os
from .forms import NewBudgetForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')

class NewBudgetCreate(LoginRequiredMixin, CreateView):
    model = Budget
    template_name = 'dashboard/budget_create.html'
    fields = [
      'name',
      'total_budget',
      'house_rent', 
      'food_budget',
      'elec_bill',
      'gas_bill',
      'water_bill',
      'other_bill'
    ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    success_url = '/dashboard'

class NewDailySpend(LoginRequiredMixin, CreateView):
    model = DailySpend
    template_name = 'dashboard/daily_spend.html'
    fields = ['date', 'amount_Spent']
    
    success_url = '/dashboard'
    
