"""caraway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.views.generic.base import TemplateView

doc_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs/')

def docs(request):
    from django import http
    return http.HttpResponsePermanentRedirect(os.path.join(request.path, 'index.html'))


swingtime_patterns = [
    url(r'^intro$', TemplateView.as_view(template_name='intro.html'), name='demo-home'),
    url(r'^karate/', include('karate.urls')),
    url(r'^admin/', admin.site.urls, name='adminsettings'),
    url(r'^docs/$', docs, name='swingtime-docs'),
    url(r'^docs/(?P<path>.*)$', serve, dict(document_root=doc_root, show_indexes=False))
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('login.urls')),
    path('', include('django.contrib.auth.urls')),
    path('calender/', RedirectView.as_view(url='/swingtime/')),
    path('swingtime/', include(swingtime_patterns)),


]
