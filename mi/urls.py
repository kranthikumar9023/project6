from django.urls import path
from mi.views import *
app_name='everything'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumra/',bumra,name='bumra'),
]