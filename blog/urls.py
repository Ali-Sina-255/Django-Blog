from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<str:slug>/', views.blogs, name='blog'),
]