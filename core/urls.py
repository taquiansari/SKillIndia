from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("",views.home, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("profile",views.profile, name='profile'),
    path("community",views.community, name='community'),
    path("register",views.register, name='register'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    path("workerregistration",views.workerregistration, name='workerregistration'),
]
