from django.shortcuts import render,redirect
from  .forms import CreateCompany,JobForm
from django.contrib.auth.decorators import login_required
from .models import Company,Job
# Create your views here.

@login_required(login_url='signin')
def dashbaord(request):
    company = Company.objects.get(user=request.user)
    context = {
        'company':company
    }
    return render(request,'dashboard.html',context)

@login_required(login_url='signin')
def edit_company(request):
    cmp = getCurrentlyLoginCompany(request.user)
    form = CreateCompany(request.POST or None,request.FILES or None,instance=cmp)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'edit_company.html',context)

@login_required(login_url='signin')
def register(request):
    template_name='create_company.html'
    if request.method=='GET':
        context = {
            'form':CreateCompany()
        }
        return render(request,template_name,context)
    else:
        form = CreateCompany(request.POST,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user=request.user
            data.save()
            return redirect('dashboard')
        else:
            return render(request,template_name,{'form':form})



@login_required(login_url='signin')
def createjob(request):
    template_name = 'create_job.html'
    if request.method=='GET':
        context = {
            'form':JobForm()
        }
        return render(request,template_name,context)
    else:
        form = JobForm(request.POST,request.FILES or None)
        if form.is_valid():
            data= form.save(commit=False)
            data.company= getCurrentlyLoginCompany(request.user)
            data.save()
            return redirect('vacancylist')
        else:
            context ={
                'form':form
            }
            return render(request, template_name, context)

@login_required(login_url='signin')
def vacancylist(request):
    template_name='vacancylist.html'
    vacancy = Job.objects.filter(company=getCurrentlyLoginCompany(request.user)).order_by('last_apply_date')
    context = {
        'vacancy':vacancy
    }
    return render(request,template_name,context)

@login_required(login_url='signin')
def editjob(request,id):
    template_name='edit_job.html'
    form =JobForm(request.POST or None,request.FILES or None,instance=Job.objects.get(id=id))
    if(form.is_valid()):
        form.save()
        return redirect('vacancylist')
    context = {
        'form': form
    }
    return render(request,template_name,context)

def removejob(request,id):
    j = Job.objects.get(id=id)
    j.delete()
    return redirect('vacancylist')

def getCurrentlyLoginCompany(user):
    return Company.objects.get(user=user)