from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreationForm
# Create your views here.
@login_required(login_url='signin')
def registeremployee(request):
    if request.method=='GET':
        context = {
            'form':EmployeeCreationForm()
        }
        return render(request,'employee_register.html',context)
    else:
        form = EmployeeCreationForm(request.POST,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user
            data.save()
            return redirect('dashboard')
        else:
            return render(request,'employee_register.html',{'form':form})