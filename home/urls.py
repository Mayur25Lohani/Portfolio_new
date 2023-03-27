from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name='home'),
    path("index.html", views.index, name='home'),
    path("team.html", views.profiles, name='team'),
    path("mentor.html", views.mentor, name='mentor'),
    path("contact.html", views.contact, name='contact')
] 