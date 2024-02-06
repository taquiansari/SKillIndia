from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("",views.HomePage, name='home'),
    path("about",views.AboutPage, name='about'),
    path("services",views.ServicePage, name='services'),
    path("contact",views.ContactPage, name='contact'),
    path("profile",views.ProfilePage, name='profile'),
]
