from django.urls import path
from event import views

urlpatterns = [
    path('<int:pk>/', views.event_view, name='event')
]