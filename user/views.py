from django.shortcuts import render

def signup(request):
    return render(request, "user/signup.html")

def user(request):
    return render(request, "user/user.html")

def list(request):
    return render(request, "user/list_user.html")


def add(request):
    return render(request, "user/add_user.html")


def edit(request):
    return render(request, "user/edit_user.html")

def delete(request):
    return render(request, "user/delete_user.html")
