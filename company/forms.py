from django import forms
from .models import Company

class CreateCompany(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    adress = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Company
        exclude =['user',]