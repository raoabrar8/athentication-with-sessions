from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from .forms import SignUpForm
from django.contrib.sessions.models import Session

def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login')
        
    else:
        form = SignUpForm()
        
    return render(request, 'authapp/signup.html', {'form':form})



def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['username'] = user.username
            return redirect('home')
        else:
            return render(request, 'authapp/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'authapp/login.html', {'form': form})
    
@login_required
def home(request):
    username = request.session.get('username')
    return render(request, 'authapp/home.html', {'username':username})



def Logout(request):
    logout(request)
    request.session.flush()
    return redirect('login')


            
                
