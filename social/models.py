from django.db import models

class SocialLink(models.Model):
    platfrom = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.platfrom