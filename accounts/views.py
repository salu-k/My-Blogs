from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Username or Password')
    return render(request,'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                messages.success(request,'Registration successful')
                return redirect('login')
            except Exception as e:
                messages.error(request,'Username already exists')
        else:
            messages.error(request,'Passwords do not match')

    return render(request,'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')