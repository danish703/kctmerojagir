from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
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
            print("useranme and paass does not match")
            return redirect('signin')


def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        u = request.POST['useranme']
        e = request.POST['email']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']
        if p1==p2:
           u = User(username=u,email=e)
           u.set_password(p1)
           u.save()
           return redirect('signin')
        else:
            print("signup vayena error aayo")
            return redirect('signup')


@login_required(login_url='signin')
def dashbaord(request):
    return render(request,'dashboard.html')
