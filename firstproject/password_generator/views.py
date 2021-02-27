from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'password_generator/home.html', {'password' : "grahamindustrial"})


def password(request):
    return render(request, 'password_generator/password.html')