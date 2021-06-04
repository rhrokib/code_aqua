from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create', views.NewBudgetCreate.as_view(), name='budget_create'),
    path('daily_spend', views.NewDailySpend.as_view(), name='daily_spend'),
]