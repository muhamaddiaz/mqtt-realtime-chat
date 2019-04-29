from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import paho.mqtt.publish as publish

# Create your views here.

def index(request):
  return render(request, 'clients/index.html')

def submitchat(request):
  if(request.method == 'POST'):
    from_name = request.POST['from']
    return HttpResponseRedirect('/clients/' + from_name)
  return HttpResponse('hello')

def chats(request, from_name):
  return render(request, 'clients/chats.html', {'from_name': from_name})

def message(request): 
  lstate = request.POST['last']
  msg = request.POST['msg']
  publish.single("group/chats", payload=msg)
  return HttpResponseRedirect('/clients/' + lstate)