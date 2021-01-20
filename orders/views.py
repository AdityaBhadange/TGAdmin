from django.shortcuts import render

# Create your views here.

def sellorder(request):
	return render(request, "orders/sellorder.html")