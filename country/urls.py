from django.urls import path
from . import views


urlpatterns = [
    path( "", views.country, name="country"),
    path( "edit/", views.edit, name="edit_country"),
    path( "list/", views.list, name="list_country"),
    path( "add/", views.add, name="add_country"),
    path( "delete/", views.delete, name="delete_country"),

]

