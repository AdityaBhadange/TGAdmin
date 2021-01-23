# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
	path("login/", views.login, name="login"),
	path("signup/", views.signup, name="signup"),
	path("base/", views.base, name="base"),
]





# urlpatterns = [
#     path('adminpanel/', login_view, name="login"),
#     path('register/', register_user, name="register"),
#     path("logout/", LogoutView.as_view(), name="logout")
# ]
