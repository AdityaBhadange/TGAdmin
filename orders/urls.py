from django.urls import path
from . import views

urlpatterns = [
    path("", views.sellorder, name="sellorder"),
]