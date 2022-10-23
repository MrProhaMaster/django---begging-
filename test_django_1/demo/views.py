from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os

# Create your views here.
def home_page(request):
    return HttpResponse("current_time/ - посмотреть текущее время;\nworkdir/ - посмотреть содержимое директории.")
def time_view(request):
    return HttpResponse(datetime.now())
def workdir(request):
    return HttpResponse(os.getcwd())