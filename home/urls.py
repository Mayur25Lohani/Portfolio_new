from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index.html", views.index, name='home'),
    path("team.html", views.profiles, name='team'),
    path("contact.html", views.contact, name='contact')
]