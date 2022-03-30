from bookingsystem.models import events
from django_filters import DateFromToRangeFilter, FilterSet

class eventFilter(FilterSet):
    Date = DateFromToRangeFilter()
    class Meta:
        model = events
        fields = '__all__'
        exclude = ['Name']

f = eventFilter({'date_after': '1867-01-01', 'date_before': '2045-02-01'})