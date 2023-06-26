from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    return render(request, 'signin.html')

@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')