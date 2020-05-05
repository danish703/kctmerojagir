from django import forms
from .models import Employee
class EmployeeCreationForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    highest_education = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    professional_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model=Employee
        exclude=['user_id',]