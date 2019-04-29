from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import paho.mqtt.publish as publish
from . import mqtt
from django.utils.safestring import mark_safe
import json

# Create your views here.

def index(request):
  return render(request, 'clients/index.html')

def submitchat(request):
  if(request.method == 'POST'):
    from_name = request.POST['from']
    return HttpResponseRedirect('/clients/' + from_name)
  return HttpResponse('hello')

def chats(request):
  return render(request, 'clients/chats.html', {})

def message(request): 
  lstate = request.POST['last']
  msg = request.POST['msg']
  publish.single("group/chats", payload=msg)
  return HttpResponseRedirect('/clients/' + lstate)

def room(request, room_name):
  return render(request, 'clients/room.html', {
    'room_name_json': mark_safe(json.dumps(room_name))
  })