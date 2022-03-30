from bookingsystem.models import events
from rest_framework import serializers

class eventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=events
        fields=['Name','City','Category','Date','Price']
