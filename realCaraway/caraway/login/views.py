from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ClassCreation
from .forms import AdminCreationForm, ClassCreationForm,ParentCreationForm

#parent 
class SignUp(generic.CreateView):
    form_class = ParentCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#admin
class SignUpAdmin(generic.CreateView):
    form_class = AdminCreationForm
    success_url = reverse_lazy('admin')
    template_name = 'signupAdmin.html'

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
