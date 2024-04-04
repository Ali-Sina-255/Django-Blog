from django.shortcuts import render
from django.http import HttpResponse

def dashborad(request):
    return render(request,'dashborad/dashborad.html')