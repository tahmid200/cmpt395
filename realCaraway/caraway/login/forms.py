from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

user = get_user_model()

class ParentCreationForm(UserCreationForm):
    username = forms.CharField(label = 'Username')
    first_name = forms.CharField(label = 'First Name')
    last_name = forms.CharField(label = 'Last Name')
    email = forms.CharField(label = 'Email')
    password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)
    children1 = forms.CharField(label = 'Child')
    children2 = forms.CharField(label = 'Child')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def clean_children1(self):
        children1 = self.cleaned_data['children'].lower()
        r = User.objects.filter(children1=children1)
        if r.count():
            raise ValidationError("Children already exists")
        return children1

    def clean_children2(self):
        children2 = self.cleaned_data['children'].lower()
        r = User.objects.filter(children2=children2)
        if r.count():
            raise ValidationError("Children already exists")
        return children2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            self.cleaned_data['children1'],
            self.cleaned_data['children2'],
        )
        return user


#parent
#class ParentCreationForm(UserCreationForm):
 #   children1 = forms.CharField(label = 'child')
  #  children2 = forms.CharField(label = 'child')
#
 #   class Meta(UserCreationForm.Meta):
  #      model = CustomUser
   #     fields = (
    #        'username',
     #       'first_name',
      #      'last_name',
       #     'email',
        #    'password1',
         #   'password2',
          #  'children1',
           # 'children2',
       # )
    #def save(self,commit = True):
     #   user = super(ParentCreationForm,self).save(commit = False)
      #  user.children1['children1']
       # user.children2['children2']
    
        #if commit:
         #   user.save()

        #return user
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
        user = super(ParentCreationForm, self).save(commit=False)


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



#class ClassCreationForm(forms.ModelForm):
#    class Meta:
#        model = CustomUser
#        widgets = {
#          'classroom': forms.Textarea(attrs={'rows':1, 'cols':85}),
#        }