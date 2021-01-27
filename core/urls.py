# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from product import views
# from orders import views as orders_views


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("auth/", include("authentication.urls")), # Auth routes - login / signup
    path("", views.dashboard, name="dashboard"),
    path("product/", include("product.urls")),
    path("commission/", include("commission.urls")),
    path("groups/", include("groups.urls")),
    path("payment/", include("payment.urls")),
    path("keywords/", include("keywords.urls")),
]
