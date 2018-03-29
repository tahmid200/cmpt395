from datetime import datetime, timedelta
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render

from swingtime import models as swingtime
from login.models import ParentCreation, CustomUser




def event_type(request, abbr):
    event_type = get_object_or_404(swingtime.EventType, abbr=abbr)
    now = datetime.now()
    occurrences = swingtime.Occurrence.objects.filter(
        event__event_type=event_type,
        start_time__gte=now,
        start_time__lte=now+timedelta(days=+30)
    )
    return render(request, 'karate/upcoming_by_event_type.html', {
        'occurrences': occurrences,
        'event_type': event_type
    })


def KarateHours(request):
    User = ParentCreation.objects.all()
    #username = request.user
    #email1 = request.user.last_name
    #curent_hours = request.user.curent_hours
    #userstuff = []
    #length = len(user)
    #for i in range(length):
     #   userstuff.append(user[i])
    return render(request, 'karate.html', {'User': User})