from django.shortcuts import render
from blogcatagory.models import Category, Blog
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def dashboard(request):
    all_category = Category.objects.all().count()
    all_blog =  Blog.objects.all().count()
    context = {
        "all_category": all_category,
        "all_blog": all_blog,
    }
    return render(request,'dashboard/dashboard.html', context)


def categories(request):
    return render(request, 'dashboard/category.html')