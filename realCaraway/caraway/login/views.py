import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import CsrfViewMiddleware
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import ListView
from .models import ParentCreation
from swingtime.models import *
from swingtime.views import *
from swingtime.forms import *
from .forms import AdminCreationForm, ClassCreationForm, ParentCreationForm, User,ParentUserCreationForm


from datetime import datetime, timedelta
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render

from swingtime import models as swingtime
from django.db import models
from login.models import ParentCreation, CustomUser



#rawdata = EventType.objects.all()
#parent
#----------------------------------------------------------------------------------------
def SignUp(request):

    if request.method == 'POST':
        form = ParentUserCreationForm(request.POST)
        parent = ParentCreationForm(request.POST)
        if form.is_valid() and parent.is_valid():
            form.save()
            username = request.POST.get('username','')
            first_name = request.POST.get('first_name','')
            email = request.POST.get('email','')
            children1 = request.POST.get('children1','')
            children2 = request.POST.get('children2','')
            last_name = request.POST.get('last_name','')
            #password2 = request.POST.get('password2','')

            obj = ParentCreation(username = username,first_name = first_name,email=email,children1=children1,children2=children2,last_name=last_name)
            messages.success(request, "Success!")
            obj.save()
            return HttpResponseRedirect('/users/signup')
    else:
       
        #keep----------------------------
        form = ParentUserCreationForm()
        parent = ParentCreationForm()
        #--------------------------------

    messages.success(request, "")
    return render(request, 'signup.html', {'form': form})


#-------------------------------------------------------------------------------------------------
#admin
class SignUpAdmin(generic.CreateView):
    form_class = AdminCreationForm
    success_url = reverse_lazy('admin')
    template_name = 'signupAdmin.html'


#class-------------------------------------------------------------------------------------------

def SignUpClass(request):

    classinfo = EventType.objects.all()

    length = len(classinfo)
    classes = []
    for i in range(length):
        classes.append(classinfo[i])
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClassCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # redirect to a new URL:

            classroom = request.POST.get('classroom','')
            classObj = EventType(label = classroom)
            #counter = EventType.objects.get(label=classroom)
            #classObj = EventType(col = length -1 )
            classObj.col = length
            #counter.save()
            classObj.save()

            #messages.success(request, "Success!")

            return HttpResponseRedirect('/users/signup/class/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClassCreationForm()
    

    #messages.success(request, "")
    return render(request, 'signupClass.html', {'classes':classes , 'form': form})




@login_required
def Home(request):
    if request.user.is_superuser:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/swingtime/karate/')

#-------------------------------------------------------------------------------------------------
@login_required
def HomeTile(request):
    User = ParentCreation.objects.all()
    length = len(User)
    for i in range(length):
        if request.user.username == User[i].username:
            hours = User[i].curent_hours
            total = User[i].total_hours
    if request.user.is_superuser:
        return render(request, 'homeTile.html')
    elif request.user.is_staff:
        return HttpResponseRedirect('/swingtime/karate/')
    else:
        return render(request, 'parentTile.html', {'hours': hours, 'total': total})
#-------------------------------------------------------------------------------------------------
@login_required
def ParentTile(request):
    User = ParentCreation.objects.all()
    length = len(User)
    for i in range(length):
        if request.user.username == User[i].username:
            hours = User[i].curent_hours
            total = User[i].total_hours
    if request.user.is_superuser:
        return render(request, 'homeTile.html')
    elif request.user.is_staff:
        return HttpResponseRedirect('/swingtime/karate/')
    else:
        return render(request, 'parentTile.html', {'hours': hours, 'total': total})
#--------------------------------------------------------------------------------------------

def UserHours(request):
    User = ParentCreation.objects.all()
    length = len(User)
    return render(request, 'userhours.html', {'User': User, 'length': length})



