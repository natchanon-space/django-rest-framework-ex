from django import urls
from django.urls import path, include

from . import views

urlpatterns = [
    path('calendar-list/', views.CalendarList.as_view()),
    path('<slug:calendar_slug>/events/', views.EventList.as_view()),
    path('<slug:calendar_slug>/<slug:event_slug>/', views.EventDetail.as_view())
]
