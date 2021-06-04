from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile
from .models import Budget
from django.urls import reverse_lazy


class NewBudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
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

        labels = {
            'name': 'Budget Name',
            'elec_bill': 'Electricity Bill'
        }

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)
    # success_url = '/dashboard'
