from django.urls import path
from weekday import views
from django.conf.urls import include

urlpatterns = [
    path('', views.week_view, name='week_view'),
    path('add/', views.add_eventview, name='event_view'),
    path('', include('event.urls')),
    path('delete/<int:pk>', views.delete, name='delete')
]