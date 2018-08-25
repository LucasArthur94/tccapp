from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout_app(request):
    logout(request)
    return redirect('home')
