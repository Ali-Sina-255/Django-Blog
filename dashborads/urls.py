from django.urls import path
from . import views


urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories , name='categories'),
    path('categories/add/', views.add_categories , name='add_category'),
    path('categories/edit/<str:value_form_url>/', views.edit_category , name='edit_category'),
    path('categories/delete/<str:value_form_url>/', views.delete_category , name='delete_category'),
    
]