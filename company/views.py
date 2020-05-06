from django.shortcuts import render,redirect
from  .forms import CreateCompany
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='signin')
def dashbaord(request):
    return render(request,'dashboard.html')

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