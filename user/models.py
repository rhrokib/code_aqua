from django.db import models
from django import forms
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=30)
    image = models.ImageField(default='default_profile.png',  upload_to='profile_pics')
    institution = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupation = models.CharField(max_length=30)
    phone = models.CharField(max_length=11, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    theme = models.CharField(max_length=10, choices=[('Day','Day'), ('Night','Night')], default='Day')
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
