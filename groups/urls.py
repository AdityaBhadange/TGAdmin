from groups import views as groups 
from django.urls import path, include
urlpatterns = [
path("",groups.groupmain,name="groups"),
path("add/",groups.groupadd,name="groupadd"),
path("edit/",groups.groupedit,name="groupedit"),
path('delete/',groups.groupdelete, name="groupdelete")
]