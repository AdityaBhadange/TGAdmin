from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.product, name="product"),
    path("", views.dashboard, name="dashboard"),
]