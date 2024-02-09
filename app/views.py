from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
def projects(request):
    return render(request, 'projects.html')
def blog(request): 
    return render(request, 'blog.html')
def contact(request): 
    return render(request, 'contact.html')
def projects(request): 
    return render(request, 'projects.html')
def purchase(request):
    return render(request, 'purchase.html')
def timeline(request): 
    return render(request, 'timeline.html')
def arcade(request): 
    return render(request, 'arcade.html')
def payment(request): 
    return render(request, 'payment.html')
def tetris(request): 
    return render(request, 'tetris.html')
def snake(request): 
    return render(request, 'snake.html')
def password(request): 
    return render(request, 'password.html')
def pong(request): 
    return render(request, 'pong.html')
def signup(request): 
    return render(request, 'signup.html')
def mario(request): 
    return render(request, 'mario.html')
def login(request): 
    return render(request, 'login.html')
def forgetpass(request): 
    return render(request, 'forgetpass.html')
def blogmenu(request): 
    return render(request, 'blogmenu.html')
def verification(request): 
    return render(request, 'verification.html')
def notepad(request): 
    return render(request, 'notepad.html')
def myip(request): 
    return render(request, 'myip.html')
def calculator(request): 
    return render(request, 'calculator.html')
def arcadegames(request): 
    return render(request, 'arcadegames.html')
def profile(request): 
    return render(request, 'profile.html')
def camera(request): 
    return render(request, 'camera.html')
def internetspeedtest(request): 
    return render(request, 'internetspeedtest.html')
def resetpassword(request): 
    return render(request, 'resetpassword.html')
def tools(request): 
    return render(request, 'tools.html')
def passwordgenerator(request): 
    return render(request, 'passwordgenerator.html')
def settings(request): 
    return render(request, 'settings.html')
def home(request):
    return redirect('/')

#function for register 

def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordre = request.POST['passwordre']
        
        if password == passwordre:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, "Username Already Used")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else: 
            messages.info(request, "passwords does not match")
            return redirect('register')
    else:
        return render(request, 'signup.html')
    
#function for login

def login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect ('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
# function for logout

def logout(request):
    auth.logout(request)
    return redirect('/')