from django.contrib import admin
from .models import Budget, DailySpend

# Register your models here.
admin.site.register(Budget)
admin.site.register(DailySpend)
