from django.shortcuts import render

# Create your views here.
def paymentmain(request):
    return render(request, "payment.html",)
    
