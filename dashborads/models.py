from django.db import models
from django.contrib.auth.models import User
from blogcatagory.models import Blog
from django.utils import timezone


class Comment(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.comment