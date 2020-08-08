from django import forms
from .models import student
from django.contrib.auth.models import User


class myForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ["name", "email", "password"]
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': "form-control"})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': "form-control"})
        }
