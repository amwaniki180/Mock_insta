from django.shortcuts import render
from django.http  import HttpResponse
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request,'welcome.html')