from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.SignUp.as_view(), name='signup'),
    path('home/', views.Home, name='home'),
    path('signup/admin/',views.SignUpAdmin.as_view(),name = 'admin'),
    #path('signup/class/',views.SignUpClass.as_view(),name = 'class')
    path('signup/class/',views.SignUpClass,name = 'class')
]
