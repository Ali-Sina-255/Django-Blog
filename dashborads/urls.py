from django.urls import path
from . import views


urlpatterns =[
    path('', views.dashborad, name='dashborad')
]