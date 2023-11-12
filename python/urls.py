from python.views import *
from django.urls import path
app_name='python'
urlpatterns=[
  path('functions/',functions,name='functions'),
  path('features/',features,name='features'),
]