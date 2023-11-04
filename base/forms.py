# forms.py
from django import forms
from base.models import mUsuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'password1', 'password2']

class mUsuarioCreationForm(forms.ModelForm):
    class Meta:
        model = mUsuario
        fields = ['CvUser', 'CvPerson', 'Login', 'Password', 'FecIni', 'FecFin', 'EdoCta']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
