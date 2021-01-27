from django.urls import path, include
from commission import views 
urlpatterns = [
    path('',views.commissionmain,name="commission"),
    path('group/',views.groupcommission,name="groupcommission"),
]