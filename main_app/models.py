from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    mama = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    mama = models.ForeignKey(User, on_delete=models.CASCADE)