from django.urls import path
from . import views


urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories , name='categories'),
    path('categories/add/', views.add_categories , name='add_category'),
    path('categories/edit/<str:value_form_url>/', views.edit_category , name='edit_category'),
    path('categories/delete/<str:value_form_url>/', views.delete_category , name='delete_category'),
    
    # post url
    path('posts/',views.posts, name='posts'),
    path('posts/add',views.add_posts, name='add_posts'),
    path('posts/edit_post/<str:value_form_url>/',views.edit_post, name='edit_posts'),
    path('posts/delete_post/<str:value_form_url>/',views.delete_post, name='delete_post'),
    # Users URL
    path('users/',views.users, name='users'),
    path('users/add/',views.add_new_user, name='add_user'),
    
]