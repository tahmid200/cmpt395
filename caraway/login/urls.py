from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name = 'login'),
    path('admin', views.adminMenu,name = 'adminMenu'),
    path('register', views.register,name = 'register')
]