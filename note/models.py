from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Note(models.Model):
  theme=[
    ('blue', 'Kinda Blue'),
    ('coral', 'Living Coral'),
    ('green', 'Pastel Green'),
    ('purple', 'Lavender'),
    ('white', 'Not So White'),
    ('teal', 'Ocean Green')
    ]
  
  title = models.CharField(max_length=255)
  content = models.TextField(max_length=10000, blank=True)
  date = models.DateTimeField(default=timezone.now)
  color = models.CharField(max_length=30, choices=theme, default='white', blank=True)
  completed = models.BooleanField(default=False)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('note_detail', kwargs={'pk':self.pk})
    
