from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.login, name='login'),
    path('admin', views.adminMenu, name='adminMenu'),
    path(r'register', views.register, name='register'),
]
