from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name="accounts"



urlpatterns = [
    path('accounts/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
    
]
