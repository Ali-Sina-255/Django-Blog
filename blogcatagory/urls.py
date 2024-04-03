from django.urls import path
from . import views

urlpatterns =[
    path('<int:category_id>/', views.post_by_catagory,name='category')
]