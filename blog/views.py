from django.shortcuts import render
from django.http import HttpResponse
from blogcatagory.models import Category, Blog


def home(request):
    blog_featuers = Blog.objects.filter(is_featured=True, status="Published" )
    posts = Blog.objects.filter(is_featured=False, status="Published" )
    context = {
        "blog_featuers":blog_featuers,
        "posts": posts
    }
    return render(request, 'blog/home-blogs.html', context)


def blogs(request, slug):
    try:
        single_post = Blog.objects.get(slug=slug, status='Published')
    except:
        return HttpResponse(f"post with is {slug} is not in the databaes .")
    context = {
        "single_post":single_post
    }
    return render(request, 'blog/blog_detail.html', context)