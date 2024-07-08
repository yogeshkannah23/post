from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from posts.models import *
from django.urls import *
# Create your views here.

app_name = "posts"

def index(request):
    return render(request,"base.html",{})

def detail(request):
    post = Post.objects.all()
    return render(request,'post/post.html',{'posts':post})

def add_post(request):
    if request.method == "POST":
        print("Post method")
        name =  request.POST['singer_name']
        print(name)
        if 'image' in request.FILES:
            image = request.FILES['image']
        description = request.POST['description']

        new_post = Post.objects.create(name=name,image=image,description=description)

    return render(request,'post/add_post.html')