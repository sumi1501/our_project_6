from os import name
from parres.views import *
from django.urls import path
app_name='fav'
urlpatterns=[
    path('life/',life,name='life'),
]