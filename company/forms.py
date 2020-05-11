from django import forms
from .models import Company,Job

class CreateCompany(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    adress = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Company
        exclude =['user',]


class JobForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    last_apply_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    class Meta:
        model = Job
        exclude = ['company',]