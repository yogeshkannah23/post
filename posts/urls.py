from django.shortcuts import render,redirect
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/',views.detail,name = 'posts'),
    path('add_post/',views.add_post,name = "add_post"),
]


