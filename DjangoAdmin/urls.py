from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import auth_views here
from . import views  # Ensure you have an index view

urlpatterns = [
    path('', views.index, name='index'),  # root URL
    path("__reload__/", include("django_browser_reload.urls")),
]