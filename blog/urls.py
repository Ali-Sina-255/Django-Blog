from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<str:slug>/', views.blogs, name='blog'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]