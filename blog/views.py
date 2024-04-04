from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogcatagory.models import Blog
from . froms import UserRegistrationForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



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




def register(request):
    forms = UserRegistrationForms()
    context = {
        "forms":forms
    }
    if request.method == "POST":
        forms = UserRegistrationForms(request.POST)
        if forms.is_valid():
            forms.save()
            # context["messages"] = "User Registration was successfull."
            print(forms.errors)
            context["messages"] = "your registration we successful"
        else:
            print(forms.errors)
    else:
        forms = UserRegistrationForms()
   
    return render(request, "account/register.html", context)


def login(request):
    if request.method == "POST":
        forms = AuthenticationForm(request,request.POST)
        if forms.is_valid():
            useranme = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = auth.authenticate(useranme=useranme, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
        else:
            print(forms.errors)
            
    else:
        forms = AuthenticationForm()
    context = {
        "forms": forms
    } 
    return render(request, 'account/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('login')