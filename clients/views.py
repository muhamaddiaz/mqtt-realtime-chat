from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("HIIII DJANGO")

def chats(request, your_name):
  return render(request, 'clients/index.html', {'name': your_name})