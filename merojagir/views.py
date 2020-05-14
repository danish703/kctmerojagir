from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .helpmethod import isemployee,isCompany
from general.models import Slider

def home(request):
    s = Slider.objects.all()
    template_name ='home.html'
    context = {
        'first':s[0],
        'otherslider':s[1:],
        'indicator':list(range(1,len(s[1:])+1))
    }
    return render(request,template_name,context)



@login_required(login_url='signin')
def dashboard(request):
    if(isemployee(request.user)):
        return redirect('emp_dashbaord')
    else:
        return redirect('dashboard')
def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST['username']
        p = request.POST['pass']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            if(isemployee(request.user)):
                return redirect('emp_dashbaord')
            if(isCompany(request.user)):
                return redirect('dashboard')
            return redirect('who')
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
            return  redirect('signin')
        else:
            context={
                'form':form
            }
            return render(request,'signup.html',context)




@login_required(login_url='signin')
def who(request):
    if(isemployee(request.user)):
        return redirect('emp_dashbaord')
    if(isCompany(request.user)):
        return redirect('dashboard')
    return render(request,'who.html')

def signout(request):
    logout(request)
    return redirect('signin')


