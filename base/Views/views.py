from base.forms import CustomUserCreation
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def register(request):
    data = {
        'form': CustomUserCreation()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreation(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')

    return render(request, 'registration/register.html', data)

def home(request):
    return render(request, 'home.html')

def exit(request):
    logout(request)
    return redirect('home')
