from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.urls import reverse

# Create your views here.


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
            else:
                user =User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print("User saved")
                return redirect('/')

        else:
            messages.info(request,"Invalid password")
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password")
            print("Invalid")
            return redirect('login2')
    else:
        return render(request,'login2.html')


