from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
  return render(request, 'clients/index.html')

def submitchat(request):
  return HttpResponse('hello')

def chats(request, from_name, to_name):
  return render(request, 'clients/chats.html', {'from_name': from_name, 'to_name': to_name})