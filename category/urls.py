from django.urls import path
from . import views

urlpatterns = [
    path("", views.category, name="category"),
    path("add_cat/",views.add_cat,  name="add_category"),
    path("edit_cat/",views.edit_cat, name="edit_category"),
    path("delete_cat/",views.delete_cat, name="delete_category"),

]