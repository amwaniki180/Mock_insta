from django.shortcuts import render
from django.http  import HttpResponse
from . import views


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')