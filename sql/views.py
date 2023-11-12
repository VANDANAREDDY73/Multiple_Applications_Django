from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def commands(request):
  return render(request,'commands.html')
def joins(request):
  return HttpResponse('<h1>Inner Join,Outer Join</h1>')
