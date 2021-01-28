from django.shortcuts import render

# Create your views here.

def product(request):
	return render(request, "product/product.html")

def add_product(request):
	return render(request, "product/add_product.html")

def edit_product(request):
	return render(request, "product/edit_product.html")

def dashboard(request):
	return render(request, "product/dashboard.html")
	