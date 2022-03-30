from django.shortcuts import render
from bookingsystem.models import events
from bookingsystem.serializers import eventSerializer
from bookingsystem.filter import eventFilter

# Create your views here.
def Event_List(request):
    if request.method == 'GET':
        print('get')
        authors = events.objects.all()
        # serializer = eventSerializer(authors, many=True)
        
        # search filter data
        myFilter = eventFilter(request.GET, queryset=authors)
        authors =  myFilter.qs
        
        context = {
            'author': authors,
            'myFilter':myFilter
        }
        # print(context)
        return render(request, 'bookinsystem/index.html', context)