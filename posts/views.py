from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from posts.models import *
from django.urls import *
from posts.forms import *
# Create your views here.

app_name = "posts"

def index(request):
    return render(request,"base.html",{})

def detail(request):
    category = Category.objects.all()
    post = Post.objects.all()
    if request.method == 'post':
        category_id = request.POST['category']
        post = Post.objects.all(category_id=category_id)
        return render(request,'post/post.html',{'posts':post,'category':category})
    print(post)
    return render(request,'post/post.html',{'posts':post,'category':category})

def add_post(request):
    category = Category.objects.all()
    if request.method == "POST":
        print("Post method")
        name =  request.POST['singer_name']
        category_id = request.POST['category']
        print(name)
        if 'image' in request.FILES:
            image = request.FILES['image']
        description = request.POST['description']
        
        Post.objects.create(name=name,image=image,description=description,category_id=category_id)

    return render(request, 'post/add_post.html', {'category':category})

def login(request):

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            cleaned_data = form.cleaned_data
            review = Review(user_name=cleaned_data["user_name"],address=cleaned_data["address"],feedback=cleaned_data["feedback"],ratings=cleaned_data["ratings"])
            review.save()
            return HttpResponse("Valid Form")
      
    else:
        form = ReviewForm()
    return render(request,'post/login.html',{'form':form})
