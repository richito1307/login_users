# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django.contrib.auth.forms import PasswordChangeForm

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','cvPersona', 'is_active', 'date_joined','dateEnd', 'password1', 'password2']
    
        widgets = {
            'dateEnd': forms.SelectDateWidget(),
            #'is_active': forms.CheckboxInput(attrs={'disabled': 'disabled'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class CustomPasswordChangeForm(PasswordChangeForm):
    show_password = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'show-password'}),
        label='Mostrar contraseña'
    )