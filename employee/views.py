from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreationForm,SkillForm
from .models import Employee,Skill
# Create your views here.

@login_required(login_url='signin')
def dashbaord(request):
    template_name ='employee_dashboard.html'
    emp = Employee.objects.get(user_id=request.user)
    form = SkillForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.employee=emp
        data.save()
        return redirect('emp_dashbaord')
    skill = Skill.objects.filter(employee=emp)
    context = {
        'info':Employee.objects.get(user_id=request.user),
        'form':SkillForm(),
        'skill':skill,
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

def edit_employee(request):
    template_name = 'employee_edit.html'
    emp = Employee.objects.get(user_id=request.user)
    form = EmployeeCreationForm(request.POST or None,request.FILES or None,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('emp_dashbaord')
    context = {
        'form':form
    }
    return render(request,template_name,context)

def removeskill(request,id):
    s = Skill.objects.get(id=id)
    s.delete()
    return redirect('emp_dashbaord')