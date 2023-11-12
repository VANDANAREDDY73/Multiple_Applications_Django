from webtech.views import *
from django.urls import path
app_name='webtech'
urlpatterns=[
  path('css/',css,name='css'),
  path('html/',html,name='html'),
]