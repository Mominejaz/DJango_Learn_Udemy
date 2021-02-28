from django.shortcuts import render

import random
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'password_generator/home.html', {'password' : "grahamindustrial"})


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    thePassword = ''

    for x in range(length):
        thePassword += random.choice(chars)


    return render(request, 'password_generator/password.html', {'password': thePassword})



def about(request):
    return render(request, 'password_generator/about.html')
