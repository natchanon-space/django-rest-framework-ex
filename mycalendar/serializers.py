from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Calendar, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "description",
            "start_date",
            "end_date"
        )

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = (
            "id",
            "name",
            "slug"
        )