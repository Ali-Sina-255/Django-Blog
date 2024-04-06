from django.shortcuts import render, redirect
from . models import Category, Blog


def post_by_catagory(request, category_id):
    categorys = Blog.objects.filter(status= 'Published', category= category_id)
    try:
        category_name = Category.objects.get(pk= category_id)
    except Category.DoesNotExist:
        return redirect("home")
        
    return render(request, 'blog/category-post.html',{
        'categorys': categorys,
        "category_name":category_name
    })



