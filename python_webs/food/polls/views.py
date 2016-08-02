#coding=utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
  now=datetime.datetime.now()
  html="<html><body>现在时刻：%s.</body></html>" %now
  return HttpResponse(html)

def hours_ahead(request,offset):
  offset = int(offset)
  dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
  html = "<html><body> In %s hours it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)