from django.urls import path
from . import views

urlpatterns = [
	path("", views.dashboard, name="dashboard"),
    path("home/", views.product, name="product"),
    path("add/", views.add_product, name="add_product"),
    path("edit/", views.edit_product, name="edit_product"),
]