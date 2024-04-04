from django.shortcuts import render
from blogcatagory.models import Blog
from django.db.models import Q

# Create your views here.
def search(request):
    keywords =  request.GET.get('keyword')
    search_result = Blog.objects.filter(Q(title__icontains = keywords) | 
                                        Q(short_description__icontains=keywords)|
                                        Q(blog_body__icontains = keywords), status='Published')
    return render(request, 'blog/search.html',{
        'search_result': search_result,
        "keywords":keywords
    })