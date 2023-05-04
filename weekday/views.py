from django.shortcuts import render
from weekday.models import Week
from event.models import Event

def week_view(request):
    week_list = Week.objects.order_by('week_id')
    event_list = Event.objects.order_by('event_id')
    list_dicts = {'week': week_list, 'event': event_list}
    return render(request, 'weekday/index.html', context = list_dicts)