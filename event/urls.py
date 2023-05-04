from django.urls import path
from event import views

urlpatterns = [
    path('', views.event_view, name='event')
]