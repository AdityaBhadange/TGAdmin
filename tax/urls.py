from django.urls import path
from . import views

urlpatterns = [
    path("", views.tax, name="tax"),
    path("list/", views.list, name="list"),
]

