from django.conf.urls import url
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('signup/',views.SignUp, name='signup'),
    path('home/', views.Home, name='home'),
    path('hometile/', views.HomeTile, name='tile menu'),
    path('parenttile/', views.ParentTile, name = 'parent menu'),
    path('signup/admin/',views.SignUpAdmin.as_view(),name = 'admin'),
    url(r'^builtinadminredirect$', RedirectView.as_view(url='/admin'), name = 'adminsettings'),
    #path('signup/class/',views.SignUpClass.as_view(),name = 'class'),
    path('signup/class/',views.SignUpClass,name = 'class'),
    path('hometile/hours',views.UserHours,name = 'userhours'),
    #url(r'^userhours$/', views.UserHours, name = 'userhours'),


]
