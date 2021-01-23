# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
# from product import views as product_views
# from orders import views as orders_views


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("auth/", include("authentication.urls")), # Auth routes - login / signup
    path("", include("app.urls")),             # UI Kits Html files
    path("product/", include("product.urls"), name="product"),
]
