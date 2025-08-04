from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=100)

def __str__(self):
    return self.name

class Blog(models.Model):
    title= models.CharField(max_length=255)
    content= models.TextField()
    created_at= models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.name

