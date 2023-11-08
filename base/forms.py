# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

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

