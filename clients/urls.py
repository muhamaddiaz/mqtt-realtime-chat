from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.submitchat, name="submitchat"),
    path('<str:from_name>/<str:to_name>/', views.chats, name='chats')
]