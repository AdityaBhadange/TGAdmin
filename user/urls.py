from django.urls import path
from user import views

urlpatterns = [
    path("", views.user, name="user"),
    path("signup/", views.signup, name="signup"),
    path("notification/", views.notification, name="notification"),
]
