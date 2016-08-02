#coding=utf-8

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def home(request):
  html='''<html>
       <body>
       <h1>welcome to django homepage</h1>
       <h2><a href='/admin'>admin page</h2>
       <h2><a href='/blog'>blog page</h2>
       <h2><a href='/recipe'>recipe page</h2>
       </body>
       </html>'''
  return HttpResponse(html)

