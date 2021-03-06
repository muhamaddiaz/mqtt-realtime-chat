from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.utils.safestring import mark_safe
import json

# Create your views here.

def index(request):
  return render(request, 'clients/index.html')

def submitchat(request):
  if(request.method == 'POST'):
    from_name = request.POST['from']
    return HttpResponseRedirect('/clients/' + from_name + '/chat')
  return HttpResponse('hello')

def chats(request, your_name):
  return render(request, 'clients/chats.html', {
    'your_name': mark_safe(json.dumps(your_name))
  })

def message(request): 
  lstate = request.POST['last']
  msg = request.POST['msg']
  publish.single("group/chats", payload=msg)
  return HttpResponseRedirect('/clients/' + lstate)

def room(request, your_name, room_name):
  return render(request, 'clients/room.html', {
    'room_name_json': mark_safe(json.dumps(room_name)),
    'your_name': mark_safe(json.dumps(your_name)),
    'my_name': your_name
  })