from django.shortcuts import render
from django.http  import HttpResponse
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    image_form = PostForm()
    images = Post.objects.all()
    commentform = CommentForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.post(form)
    return render(request, 'landing.html', locals())
