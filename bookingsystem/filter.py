from dataclasses import field, fields
from pyexpat import model
import django_filters
from bookingsystem.models import events

class eventFilter(django_filters.FilterSet):
    
    class Meta:
        model = events
        fields = '__all__'
        exclude = ['EventName']
