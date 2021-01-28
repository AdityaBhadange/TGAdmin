from django.shortcuts import render


def tax(request):
	return render(request, "tax/tax.html")

def list(request):
	return render(request,"tax/list.html")