from django.contrib import admin
from django.urls import path, include
from . import views

app_name="food_app"



urlpatterns = [
    path('', views.index, name="index"),
    path("menu/",views.menu, name="menu"),
    path("menu_details/<int:food_id>",views.menu_details, name="menu_details"),
]
