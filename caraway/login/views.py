from django.shortcuts import render

from django.http import HttpResponse
# login request view
def login(request):
    return render(request, 'login/index.html')
# admin menu reqquest
def adminMenu(request):
    return render(request, 'login/menu.html')
#restration page request
def register(request):
    return render(request, 'login/register.html')