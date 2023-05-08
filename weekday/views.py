from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from weekday.models import Week
from event.models import Event

def week_view(request):
    eventSun = Event.objects.filter(day=1)
    eventMon = Event.objects.filter(day=2)
    eventTues = Event.objects.filter(day=3)
    eventWed = Event.objects.filter(day=4)
    eventThurs = Event.objects.filter(day=5)
    eventFri = Event.objects.filter(day=6)
    eventSat = Event.objects.filter(day=7)
    event_dict = {'eventsun': eventSun, 'eventmon': eventMon,'eventtues': eventTues,
                  'eventwed': eventWed,'eventthurs': eventThurs,'eventfri': eventFri,'eventsat': eventSat}
    return render(request, 'weekday/index.html', context = event_dict)

def add_eventview(request):
    return(request, 'weekday/add_event.html')

def add_weekday(request, day, start, end, title, description):
    Week.objects.create(day, start, end, title, description)
    Week.save()
    return HttpResponseRedirect('weekday/index.html', args=(day, start, end, title, description))

def delete(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return HttpResponseRedirect('')