# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse #plus

from feedback.models import *
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def message(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})

def folder(request):
    msg = 'Folder'
    return render(request, 'folder/index.html', {'message': msg})

def array(request):
    msg = {1,2,3,4}
    return render(request, 'array.html', {'message': msg})

def select(request):
    for f in Feedback.objects.all():
        msg += str(f.title) + ' : ' + f.content + '\n'

    return render(request, 'array.html', {'message': msg})
