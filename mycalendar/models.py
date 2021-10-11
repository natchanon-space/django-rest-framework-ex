from django.db import models
from django.db.models.base import Model


class Calendar(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.slug}/'


class Event(models.Model):
    calendar = models.ForeignKey(Calendar, related_name="calendars", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.calendar.slug}/{self.slug}/'
    
