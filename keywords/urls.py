from django.urls import path, include
from keywords import views
urlpatterns = [
    path("",views.keywordsmain,name="keywords")
]
