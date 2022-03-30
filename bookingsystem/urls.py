from django.urls import path
from bookingsystem import views

urlpatterns = [
    path('', views.Event_List, name='eventList')
]
