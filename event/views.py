from django.shortcuts import render
from event.models import Event

def event_view(request, pk):
    event_list = Event.objects.get(pk = pk)
    event_dict = {'event': event_list}
    return render(request, 'event/event_detail.html', context = event_dict)
