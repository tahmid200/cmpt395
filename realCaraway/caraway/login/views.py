from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import ClassCreation, ParentCreation
from .forms import AdminCreationForm, ClassCreationForm, ParentCreationForm


#def SignUp(request):
 #   if request.method == 'POST':
  #      f = ParentCreationForm(request.POST)
   #     if f.is_valid():
    #        f.save()
     #       messages.success(request, 'Account Created!')
      #      return redirect('home')
    #else:
     #   f = ParentCreationForm()

    #return render(render(request, 'signup.html' , {'form': f}))




#parent


#class SignUp(generic.CreateView):
 #   form_class = ParentCreationForm
  #  success_url = reverse_lazy('login')
   # template_name = 'signup.html'


def SignUp(request):
    if request.method == 'POST':
        form = ParentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username' , '')
            usernameObj = ParentCreation(username = username)
            usernameObj.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')

    else:
        form = ParentCreationForm()

    return render(request, 'signup.html', {'form': form})



#admin
class SignUpAdmin(generic.CreateView):
    form_class = AdminCreationForm
    success_url = reverse_lazy('admin')
    template_name = 'signupAdmin.html'
#class
def SignUpClass(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClassCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # redirect to a new URL:
            classroom = request.POST.get('classroom','')
            classObj = ClassCreation(classroom = classroom)
            classObj.save()

            return HttpResponseRedirect('/users/signup/class/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClassCreationForm()

    return render(request, 'signupClass.html', {'form': form})




def Home(request):
    return render(request, 'home.html')
