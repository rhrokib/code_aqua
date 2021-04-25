from django.urls import path
from . import views

urlpatterns = [
	path('', views.api_overview, name="api_overview"),
	path('users', views.user_list, name="users_api_list"),
	path('user/<str:pk>', views.user_detail, name="user_api_detail"),
	path('create', views.user_create, name="user_api_create"),
	path('update/<str:pk>', views.user_update, name="user_api_update"),
	path('delete/<str:pk>', views.user_delete, name="user_api_delete"),
]
