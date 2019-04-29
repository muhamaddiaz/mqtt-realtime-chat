from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitchat/', views.submitchat, name="submitchat"),
    path('message/', views.message, name="message"),
    path('<str:from_name>/', views.chats, name='chats')
]