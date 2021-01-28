from django.shortcuts import render


def country(request):
	return render(request, "country/country.html")



def edit(request):
	return render(request, "country/edit.html")


def delete(request):
	return render(request, "country/delete.html")



def combination_del(request):
	return render(request, "country/combination_del.html")


def combination(request):
	return render(request, "country/combination.html")


def list_country(request):
	return render(request, "country/list.html")