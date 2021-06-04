from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Budget, DailySpend
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from PIL import Image
import os
from .forms import NewBudgetForm, DailySpendForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    context = {}
    total_spent = 0
    total_daily_spent = 0
    count = 0
 
    context['budget'] = Budget.objects.get(owner=request.user)
    context['daily'] = DailySpend.objects.filter(owner=request.user)
    
    for i in context['daily']:
        total_daily_spent += i.amount_Spent
        count += 1

    if count > 0:
        avg = float(total_daily_spent) / count
    else: 
        avg = 0
    total_spent = (total_daily_spent + context['budget'].food_budget +
                context['budget'].house_rent + context['budget'].elec_bill + context['budget'].gas_bill +
                context['budget'].water_bill + context['budget'].other_bill)

    context['cur_bal'] = context['budget'].total_budget - total_spent
    context['avg'] = avg
    context['count'] = count
    


    return render(request, 'dashboard/index.html', context)


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

class BudgetUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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
    
    def test_func(self):
        budget = self.get_object()
        if self.request.user == budget.owner: 
            return True
        return False
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    success_url = '/dashboard'
               

class NewDailySpend(LoginRequiredMixin, CreateView):
    model = DailySpend
    template_name = 'dashboard/daily_spend.html'
    fields = ['date', 'amount_Spent']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    success_url = '/dashboard'


@login_required
def daily_spend(request):
    if request.method == 'POST':
        form = DailySpendForm(request.POST, instance=request.user)
        if form.is_valid():
            d = DailySpend(date=form.cleaned_data['date'], amount_Spent=form.cleaned_data['amount_Spent'], owner=request.user)
            d.save()
            return redirect('dashboard')
    else:
        form = DailySpendForm()

    context = {'form': form}
    return render(request, 'dashboard/daily_spend.html', context)
