
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#parent
class ParentCreationForm(UserCreationForm):
    children1 = forms.CharField(label = 'child')
    children2 = forms.CharField(label = 'child')

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


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class ClassCreationForm(forms.Form):
    class_name = forms.CharField(label = 'Class Name',max_length=50)



#class ClassCreationForm(forms.ModelForm):
#    class Meta:
#        model = CustomUser
#        widgets = {
#          'classroom': forms.Textarea(attrs={'rows':1, 'cols':85}),
#        }