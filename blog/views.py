from django.shortcuts import render
from django.http import HttpResponse
from blogcatagory.models import Category, Blog


def home(request):
    categorys = Category.objects.all()
    blog_featuers = Blog.objects.filter(is_featured=True, status="Published" )
    posts = Blog.objects.filter(is_featured=False, status="Published" )
    context = {
        'categorys': categorys,
        "blog_featuers":blog_featuers,
        "posts": posts
    }
    return render(request, 'blog/home-blogs.html', context)