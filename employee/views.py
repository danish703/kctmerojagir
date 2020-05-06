from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreationForm
from .models import Employee
# Create your views here.

@login_required(login_url='signin')
def dashbaord(request):
    template_name ='employee_dashboard.html'
    context = {
        'info':Employee.objects.get(user_id=request.user)
    }
    return render(request,template_name,context)

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
            return redirect('emp_dashbaord')
        else:
            return render(request,'employee_register.html',{'form':form})