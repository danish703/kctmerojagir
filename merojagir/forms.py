from django.contrib.auth.forms import UserCreationForm
from django import forms
class CustomUserCreationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Password Confirmation")
