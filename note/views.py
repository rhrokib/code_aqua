from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Note
from django.contrib.auth.decorators import login_required


@login_required
def my_notes(request):
    context = {}
    
    try:
        context['notes'] = Note.objects.filter(author=request.user)
    except Note.DoesNotExist:
        context['notes'] = None
        
    
    return render(request, 'note/notes.html', context)



class AllNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'note/notes.html'
    context_object_name = 'notes'
    ordering = ['-date']
    paginate_by = 10
    
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Note.objects.filter(author=user).order_by('-date')

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note/note_create.html'
    
    fields =['title', 'color', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # success_url = '/notes'
    
class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name='note/note_create.html'
    fields = ['title', 'color', 'completed', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False
    success_url = '/notes'
    
    