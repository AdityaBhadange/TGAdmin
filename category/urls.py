from django.urls import path
from category import views

urlpatterns = [
    path("", views.category, name="category"),
    path("delete_cat/",views.delete_cat),
    path("list_cat/",views.list_cat),
]