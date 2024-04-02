from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'catagories'
    
    def __str__(self) -> str:
        return self.category_name

# def image_director_path(instance, image):
#     return "user_{0} / {1}".format(instance.user.id, image)


STATUS_CHOICES = (
    ("Draft","Draft"),
    ("Published","Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    featured_image = models.ImageField(upload_to='images/%Y/%m/%d',default='default.jpg')
    short_description = models.CharField(max_length=500)
    blog_body = models.TextField()
    status = models.CharField(max_length=255,choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Blogs'
    
    def __str__(self) -> str:
        return self.title
    
class Article(models.Model):
    article_name = models.CharField(max_length=255)