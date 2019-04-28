from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:your_name>/', views.chats, name='chats')
]