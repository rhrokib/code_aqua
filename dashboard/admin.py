from django.contrib import admin
from .models import Budget, Person, PerPersonMeal, DailySpend

# Register your models here.
admin.site.register(Budget)
admin.site.register(Person)
admin.site.register(PerPersonMeal)
admin.site.register(DailySpend)
