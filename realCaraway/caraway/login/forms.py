from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required


User = get_user_model()

#Parent
#-----------------------------------------------------------------------------------------
class ParentCreationForm(UserCreationForm):
    children1 = forms.CharField(label = 'children1')
    children2 = forms.CharField(label = 'children2') 
    email = forms.EmailField(required = True) 

    class Meta(UserCreationForm):  
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'children1',
            'children2'  
        )
    def save(self, commit=True):
        user = super(ParentCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.children1 = self.cleaned_data['children1']
        user.children2 = self.cleaned_data['children2']


        if commit:
            user.save()

        return user
#------------------------------------------------------------------------------------------
#Admin
class AdminCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
)

    def save(self, commit=True):
        user = super(AdminCreationForm, self).save(commit=False)


        if commit:
            user.is_superuser=True
            user.is_staff=True
            user.save()


        return user



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        
#class ------------------------------------------------------------------------------------------
class ClassCreationForm(forms.Form):
    classroom = forms.CharField(label = 'Class Name',max_length=50)
#---------------------------------------------------------------------------------------------