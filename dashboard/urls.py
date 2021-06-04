from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create', views.NewBudgetCreate.as_view(), name='budget_create'),
    path('update/<str:pk>', views.BudgetUpdate.as_view(), name='budget_update'),
    path('daily_spend', views.daily_spend, name='daily_spend'),
]