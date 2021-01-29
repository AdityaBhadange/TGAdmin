from django.urls import path
from . import views

urlpatterns = [
    path("", views.tax, name="tax"),
    path("add/", views.add_tax, name="add_tax"),
    path("edit/", views.edit_tax, name="edit_tax"),
    path("delete/", views.delete_tax, name="delete_tax"),
    path("list/", views.list, name="list_tax"),
]

