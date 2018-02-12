from django.shortcuts import render

from django.http import HttpResponse

def login(request):
    return render(request, 'login/index.html')

def adminMenu(request):
    return render(request, 'login/menu.html')

def register(request):
    return render(request, 'login/register.html')