from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("team.html", views.profiles, name='home'),
     path("contact.html", views.contact, name='home')
]