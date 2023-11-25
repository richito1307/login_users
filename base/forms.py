# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from datetime import datetime

class CustomUserCreation(UserCreationForm):
    date_joined = forms.DateField(label='Fecha Inicial', widget=forms.SelectDateWidget())

    class Meta:
        model = User
        fields = ['username', 'cvPersona', 'date_joined', 'dateEnd', 'is_active', 'password1', 'password2']

        widgets = {
            'dateEnd': forms.SelectDateWidget(),
        }

        labels = {
            'cvPersona': 'Persona',
            'dateEnd': 'Fecha Final',
        }

    def clean_date_joined(self):
        date_joined = self.cleaned_data['date_joined']
        current_date = timezone.localtime(timezone.now()).date()
        

        if date_joined < current_date:
            raise forms.ValidationError("La fecha inicial no puede ser menor a la fecha actual")
        return date_joined
    
    def clean_dateEnd(self):
        date_joined = self.cleaned_data.get('date_joined')
        dateEnd = self.cleaned_data['dateEnd']

        if date_joined is not None:
            if isinstance(date_joined, datetime):
                date_joined = date_joined.date()

            if isinstance(dateEnd, datetime):
                dateEnd = dateEnd.date()

            if dateEnd < date_joined:
                raise forms.ValidationError("La fecha final no puede ser menor a la fecha inicial")
        return dateEnd


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

class CustomUserEditForm(forms.ModelForm):
    date_joined = forms.DateField(label='Fecha Inicial', widget=forms.SelectDateWidget())

    class Meta:
        model = User
        fields = ['username', 'cvPersona', 'date_joined', 'dateEnd', 'is_active']

        widgets = {
            'dateEnd': forms.SelectDateWidget(),
        }

        labels = {
            'cvPersona': 'Persona',
            'dateEnd': 'Fecha Final',
        }
    
    def clean_dateEnd(self):
        date_joined = self.cleaned_data['date_joined']
        dateEnd = self.cleaned_data['dateEnd']

        if isinstance(date_joined, datetime):
            date_joined = date_joined.date()

        if isinstance(dateEnd, datetime):
            dateEnd = dateEnd.date()

        if dateEnd < date_joined:
            raise forms.ValidationError("La fecha final no puede ser menor a la fecha inicial")
        return dateEnd