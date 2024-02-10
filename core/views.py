from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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

def register(request):
    
    if request.method == 'POST' :
        username = request.POST['username']
        phoneno = request.POST['phoneno']
        passw = request.POST['passw']
        
        myuser = User.objects.create_user(username, phoneno, passw)
        myuser.save()
        
        messages.success(request, "Your Account has been succesfully created.")
        
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    
    if request.method == 'POST' :
        phoneno = request.POST['phoneno']
        passw = request.POST['passw']
        
        user = authenticate(phoneno = phoneno, password = passw)
        
        if user is not None: 
            login(request, user)
            username = username
            return render(request,'home.html',{'username': username})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')
    
    return render(request, 'login.html')

def logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def workerregistration(request):
    return render(request, 'workerregistration.html')