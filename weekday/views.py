from django.shortcuts import render
from django.http import HttpResponseRedirect
from weekday.models import Week
from event.models import Event

def week_view(request):
    week_list = Week.objects.order_by('week_id')
    event_list = Event.objects.order_by('event_id')
    list_dicts = {'week': week_list, 'event': event_list}
    return render(request, 'weekday/index.html', context = list_dicts)

def add_eventview(request):
    return(request, 'weekday/add_event.html')

def add_weekday(request, day, start, end, title, description):
    Week.objects.create(day, start, end, title, description)
    Week.save()
    return HttpResponseRedirect('weekday/index.html', args=(day, start, end, title, description))