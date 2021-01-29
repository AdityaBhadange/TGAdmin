from django.shortcuts import render


def country(request):
	return render(request, "country/country.html")

def edit(request):
	return render(request, "country/edit_country.html")

def list(request):
	return render(request, "country/list_country.html")

def add(request):
	return render(request, "country/add_country.html")

def delete(request):
	return render(request, "country/delete_country.html")


