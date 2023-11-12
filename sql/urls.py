from sql.views import *
from django.urls import path
app_name = 'sql'
urlpatterns = [
  path('commands/',commands,name='commands'),
  path('joins/',joins,name='joins'),
]