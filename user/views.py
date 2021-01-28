from django.shortcuts import render

def signup(request):
    return render(request, "user/signup.html")

def user(request):
    return render(request, "user/user.html")

def notification(request):
    return render(request, "user/notification.html")