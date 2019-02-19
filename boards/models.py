from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'categories'
	
    	
    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='category')
    last_update = models.DateTimeField(auto_now_add=True)    
    starter = models.ForeignKey(User,related_name='category')


class Post(models.Model):
    message = models.TextField(max_length=5000)
    topic = models.ForeignKey(Topic,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User,related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
