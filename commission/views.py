from django.shortcuts import render

# Create your views here.
def commissionmain(request):

    return render(request,"commission.html")
def groupcommission(request):
    return render(request,"groupcommission.html")