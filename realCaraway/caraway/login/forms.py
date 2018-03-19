from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

class ParentCreationForm(forms.Form):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    children1 = forms.CharField(max_length=30)
    children2 = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data = super(ParentCreationForm,self).clean()
        username = cleaned_data.get('name')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        children1 = cleaned_data.get('children1')
        children2 = cleaned_data.get('children2')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not email and not username and not first_name and not last_name:
            raise forms.ValidationError("Missing Fields")

        elif password1 != password2:
            raise forms.ValidationError("Incorrect Password")


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

class ClassCreationForm(forms.Form):
    classroom = forms.CharField(label = 'Class Name',max_length=50)
