from django.shortcuts import render


def category(request):
    return render(request, "category/category.html")


def list_cat(request):
    return render(request, "category/list.html")

def delete_cat(request):
    return render(request, "category/delete_cat.html")