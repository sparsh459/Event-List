from dataclasses import field, fields
from pyexpat import model
import django_filters
from bookingsystem.models import events

class eventFilter(django_filters.FilterSet):
    # EventCity = django_filters.CharFilter(field_name='City')
    # EventDate = django_filters.CharFilter(field_name='Date')
    # EventDate = django_filters.CharFilter(field_name='Date')
    # EventPrice = django_filters.CharFilter(field_name='Price')
    # EventCategory = django_filters.CharFilter(field_name='Category')

    class Meta:
        model = events
        fields = '__all__'
        exclude = ['EventName']