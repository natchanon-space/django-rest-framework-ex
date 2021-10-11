from django.http.response import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Calendar, Event
from .serializers import CalendarSerializer, EventSerializer
from mycalendar import serializers

class CalendarList(APIView):
    def get(self, request, format=None):
        calendars = Calendar.objects.all()
        serializers = CalendarSerializer(calendars, many=True)
        return Response(serializers.data)

class EventList(APIView):
    def get_object(self, calendar_slug):
        try:
            return Event.objects.filter(calendar__slug=calendar_slug)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, calendar_slug, format=None):
        events = self.get_object(calendar_slug)
        serializers = EventSerializer(events, many=True)
        return Response(serializers.data)

class EventDetail(APIView):
    def get_object(self, calendar_slug, event_slug):
        try:
            return Event.objects.filter(calendar__slug=calendar_slug).get(slug=event_slug)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, calendar_slug, event_slug, format=None):
        events = self.get_object(calendar_slug, event_slug)
        serializers = EventSerializer(events)
        return Response(serializers.data)        