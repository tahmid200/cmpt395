from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AdminCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = AdminCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)