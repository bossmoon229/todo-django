from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("show_todos")
        else:
            messages.success(request, ("Wrong username or password"))
            return render(request, "authenticate/login.html", {"error": "Invalid credentials"})
        
    else:
        return render(request, "authenticate/login.html")
    

def logout_user(request):
    logout(request)
    messages.success(request, ("U were logout"))
    return redirect('home_page')