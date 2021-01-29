from django.shortcuts import render

def category(request):
    return render(request, "category/category.html")

def add_cat(request):
    return render(request, "category/add_category.html")

def edit_cat(request):
    return render(request, "category/edit_category.html")

def delete_cat(request):
    return render(request, "category/delete_category.html")
