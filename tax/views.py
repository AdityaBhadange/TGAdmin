from django.shortcuts import render


def tax(request):
	return render(request, "tax/tax.html")

def add_tax(request):
	return render(request, "tax/add_tax.html")

def edit_tax(request):
	return render(request, "tax/edit_tax.html")

def delete_tax(request):
	return render(request, "tax/delete_tax.html")

def list(request):
	return render(request,"tax/list_tax.html")