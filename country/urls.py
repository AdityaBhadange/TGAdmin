from django.urls import path
from . import views


urlpatterns = [
    path( "", views.country, name="country"),
    path( "edit", views.edit, name="edit"),
    path( "list", views.list_country, name="list"),
    path( "delete", views.delete, name="delete"),
    path( "combination", views.combination, name="combination"),
    path( "combination_del", views.combination_del, name="combination_del"),
]

