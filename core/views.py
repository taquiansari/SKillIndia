from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def ProfilePage(request):
    return render(request, 'profile.html')

def AboutPage(request):
    return render(request, 'about.html')

def ServicePage(request):
    return render(request, 'service.html')

def ContactPage(request):
    return render(request, 'contact.html')

# def SignupPage(request):
#     return render(request, 'service.html')

# def LoginPage(request):
#     return render(request, 'service.html')