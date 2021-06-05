from django.urls import path
from .views import (AllNotesView, NoteCreateView, NoteUpdateView, NoteDeleteView, NoteDetailView)
from . import views

urlpatterns = [
    path('', views.my_notes, name='notes'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('create', NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/update', NoteUpdateView.as_view(), name='note_update'),
    path('<int:pk>/delete', NoteDeleteView.as_view(), name='note_delete'),
]