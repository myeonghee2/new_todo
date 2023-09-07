from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from user.models import User


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return redirect('/longin/')
    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, "user/login.html/")
        
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("/todo/")
    elif request.method =="GET":
        return render(request, 'user/signup.html')
    else:
        return HttpResponse("Invalid request method", setatus=405)
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/todo/")
        else:
            return HttpResponse("Invalid auth", setatus=401)
    elif request.method == "GET":
        return render(request, "user/login.html")
    else:
        return HttpResponse("Invalid request method", setatus=405)