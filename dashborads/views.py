from django.shortcuts import render, redirect
from blogcatagory.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import AddCategoryForms
from django.http import HttpResponse

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
    return render(request, 'dashboard/categories.html')


def add_categories(request):
    forms = AddCategoryForms()
    context = {
        "forms": forms
    }
    if request.method == "POST":
        forms = AddCategoryForms(request.POST)
        if forms.is_valid():
            forms.save()
            context["messages"] = "New Category is added."
            return redirect('categories')
            
    forms = AddCategoryForms()
   
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, value_form_url):
    category = Category.objects.get(id=value_form_url)
    forms = AddCategoryForms(instance=category)
    context = {
        "forms":forms,
        "categories":category
    }
    if request.method == "POST":  
        forms = AddCategoryForms( request.POST, instance=category)
        if forms.is_valid():
            forms.save()
            context['messages'] = "Category is updated"
        else:
            print(forms.errors) 
    return render(request, 'dashboard/edit_category.html', context)


@login_required(login_url='login')
def delete_category(request, value_form_url):
    delete_category = Category.objects.get(id=value_form_url).delete()
    context = {
        "object":delete_category
    }
    return render(request, 'dashboard/delete_category.html', context)