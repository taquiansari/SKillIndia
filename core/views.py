from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def AboutPage(request):
    pass

def ServicePage(request):
    pass

def ContactPage(request):
    pass

def SignupPage(request):
    pass

def LoginPage(request):
    pass