# django-rest-framework-ex
## Getting started
```
# activate virtual environment
source venv/bin/activate
```
```
# install dependencies
pip install -r requirements.txt
```
```
# setup database
python manage.py migrate
python manage.py loaddata calendar_data
```
```
# run server and explorer api
python manage.py runserver
```
## List of Urls
```py
urlpatterns = [
    path('calendar-list/', views.CalendarList.as_view()),
    path('<slug:calendar_slug>/events/', views.EventList.as_view()),
    path('<slug:calendar_slug>/<slug:event_slug>/', views.EventDetail.as_view())
]
```