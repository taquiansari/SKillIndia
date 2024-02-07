from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def community(request):
    return render(request, 'community.html')

# def SignupPage(request):
#     return render(request, 'service.html')

# def LoginPage(request):
#     return render(request, 'service.html')