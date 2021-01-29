from django.urls import path
from user import views

urlpatterns = [
    path("", views.user, name="user"),
    path("delete/", views.delete, name="delete_user"),
    path("list/",views.list,name="list_user"),
    path("signup/", views.signup, name="signup_user"),
    path("add/",views.add, name="add_user"),
    path("edit",views.edit, name="edit_user"),

]
