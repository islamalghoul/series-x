from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser

class Series(models.Model):
    name =models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('series_detail', args=[str(self.id)])