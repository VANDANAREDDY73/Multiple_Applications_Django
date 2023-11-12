from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def functions(request):
  return render(request,'functions.html')
def features(request):
  return HttpResponse('<h1>High Level Language</h1>')