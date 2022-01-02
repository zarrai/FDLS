from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as LOGIN
from django.contrib.auth import logout as LOGOUT
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib import messages

def login(request):
    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        LOGIN(request,user)
        return redirect('home')
    
    return render(request,'login.html')

def logout(request):
    LOGOUT(request)
    return redirect('home')

def signup(request):

    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        a = request.POST['add']
        m = request.POST['mobile']
        i = request.FILES['image']


        UserModel = get_user_model()
        if not UserModel.objects.filter(username=u).exists():
            user = User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            Profile.objects.create(user=user,mobile=m,address=a,image=i)
        else:
            return render(request,'signup.html',{'error':'user already exist'})
    return render(request,'signup.html')


def home(request):
    return render(request,'home.html')