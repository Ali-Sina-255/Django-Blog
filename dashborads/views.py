from django.shortcuts import render, redirect
from blogcatagory.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import AddCategoryForms, AddPostForms
from django.http import HttpResponse
from django.template.defaultfilters import slugify


@login_required(login_url="login")
def dashboard(request):
    all_category = Category.objects.all().count()
    all_blog = Blog.objects.all().count()
    context = {
        "all_category": all_category,
        "all_blog": all_blog,
    }
    return render(request, 'dashboard/dashboard.html', context)


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
        "forms": forms,
        "categories": category
    }
    if request.method == "POST":
        forms = AddCategoryForms(request.POST, instance=category)
        if forms.is_valid():
            forms.save()
            context['messages'] = "Category is updated"
        else:
            print(forms.errors)

    return render(request, 'dashboard/edit_category.html', context)


@login_required(login_url='login')
def delete_category(request, value_form_url):
    try:
        delete_category = Category.objects.get(id=value_form_url)
    except Category.DoesNotExist:
        return HttpResponse('This category is not exist')
    if request.method == "POST":
        delete_category.delete()
        return redirect('categories')
    context = {
        "object": delete_category
    }
    return render(request, 'dashboard/delete_category.html', context)


@login_required(login_url="login")
def posts(request):
    posts =Blog.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'dashboard/post.html', context)



@login_required(login_url="login")
def add_posts(request):
    form = AddPostForms()
    context = {
        "form": form
    }
    if request.method == 'POST':
        form = AddPostForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporarily saving our data in the database we can add our custom data
            post.author =  request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            context["messages"] = "your post is saved."
    form = AddPostForms()
    
    return render(request, 'dashboard/add_posts.html', context)


def edit_post(request, value_form_url):
    try:
        post = Blog.objects.get(pk=value_form_url)
    except Blog.DoesNotExist:
        return HttpResponse("blog does not exits")
    form = AddPostForms(instance=post)
    context ={
        "form": form,
        "post":post
    }
    if request.method == "POST":
        form = AddPostForms(request.POST, request.FILES, instance=post,)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            context["messages"] = "your post is Updated."
    
    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, value_form_url):
    try:   
        post = Blog.objects.get(id=value_form_url)
    except Blog.DoesNotExist:
        return HttpResponse("this post is not in the Database")
    context = {
        "post":post
    }
    if request.method == "POST":  
        post.delete()
        context["messages"] = "Your post is deleted"
        return redirect('posts')
    return render(request, 'dashboard/delete_post.html')