from django.urls import path, include
from . import views

urlpatterns = [
    # include('django....')impelments all django authentication services to be used in html to verify users
    # need to put templates in register for autheticatin uses such as login etc. its where django automatically looks
    path('accounts/', include('django.contrib.auth.urls')),

    # admin menu pathway
    path('admin', views.adminMenu, name='adminMenu'),
    # regtration pathway
    path(r'register', views.register, name='register'),
]
