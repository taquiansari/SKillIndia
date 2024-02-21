from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from core.models import Contact

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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

def community(request):
    return render(request, 'community.html')

def register(request):
    
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        myuser = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        
        myuser.save()
        
        return redirect('loginn')
    
    return render(request, 'register.html')

def loginn(request):
    
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None: 
            auth.login(request,user)
            username = username
            return redirect('home')
        # else:
        #     messages.error(request,"Bad Credentials!")
        #     return redirect('home')
    
    return render(request, 'loginn.html')

def logout(request):
    pass
    # logout(request)
    # messages.success(request, "Logged Out Successfully!")
    # return redirect('home')

def workerregistration(request):
    return render(request, 'workerregistration.html ')

def postjob(request):
    return render(request, 'postjob.html' )