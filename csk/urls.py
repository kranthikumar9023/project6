from django.urls import path
from csk.views import *
app_name='something'
urlpatterns=[
    path('msd/',msd,name='msd'),
    path('raina/',raina,name='raina'),
]