from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import CustomUserCreationForm
def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST['username']
        p = request.POST['pass']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"username and password does not match")
            return redirect('signin')


def signup(request):
    if request.method=='GET':
        context= {
            'form':CustomUserCreationForm()
        }
        return render(request,'signup.html',context)
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully account created")
        else:
            context={
                'form':form
            }
            return render(request,'signup.html',context)



@login_required(login_url='signin')
def dashbaord(request):
    return render(request,'dashboard.html')
