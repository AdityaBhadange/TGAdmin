from django.shortcuts import render

# Create your views here.
def groupmain(request):
    return render(request,"group.html")
def groupadd(request):
    return render(request,"groupadd.html", {})
def groupedit(request):
     return render(request,"groupedit.html", {})
def groupdelete(request):
    return render(request,"groupdelete.html", {})
    
    
    