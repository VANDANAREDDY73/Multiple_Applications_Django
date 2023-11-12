from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def css(request):
  return render(request,'css.html')
def html(request):
  return HttpResponse('<h1>Hyper Text Markup Language</h1>')
