from django.contrib import admin 
from .models import Category, Blog
from . models import Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title', 'category', 'status', 'author', 'is_featured')
    list_editable = ("is_featured",)
    search_fields = ('id', 'title', 'status', 'category__category_name')

admin.site.register(Blog, BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'update_at')
    list_display_links = ('id', 'category_name')
admin.site.register(Category,CategoryAdmin )
