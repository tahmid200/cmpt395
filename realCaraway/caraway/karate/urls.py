from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.KarateHours, name='karate-home'),
    url(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='karate-event'),
    url(r'^swingtime/', include('swingtime.urls')),
]

