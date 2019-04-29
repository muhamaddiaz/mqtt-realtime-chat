from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitchat/', views.submitchat, name="submitchat"),
    path('message/', views.message, name="message"),
    path('<str:your_name>/chat/', views.chats, name='chats'),
    path('<str:your_name>/chat/<str:room_name>/', views.room, name='room')
]