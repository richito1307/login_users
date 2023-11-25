from base.forms import CustomUserCreation, LoginForm, CustomPasswordChangeForm, CustomUserEditForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.utils import timezone
from user.models import User
from mPersona.models import mPersona
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            return redirect('home')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login

def register_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreation(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = CustomUserCreation()
        return render(request, 'registration/register.html', {'form': form})
    else:
        return redirect('login')

def login_view(request):
    data = {
        'form': LoginForm(),
    }

    if request.method == 'POST':
        user_creation_form = LoginForm(data=request.POST)

        if user_creation_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            try:
                user_id = User.objects.get(username=username)
                userA = User.objects.get(id=user_id.id)
                now = timezone.now()
                if userA.dateEnd is not None:
                    if now > userA.dateEnd or userA.date_joined > now:
                        if userA.is_active:
                            userA.is_active = False
                            userA.save()
                            messages.error(request, 'Su cuenta ha sido desactivada.')
                        else:
                            messages.error(request, 'Su cuenta está desactivada. Póngase en contacto con el administrador.')
                            return redirect('login')
                    else:
                        userA.is_active = True
                        userA.save()

                if userA.is_active:
                    if user is not None:        
                        login(request, user)  
                        return redirect('home') 
                    else:
                        messages.error(request, 'Credenciales de inicio de sesión incorrectas.')

            except ObjectDoesNotExist:
                messages.error(request, 'El usuario no existe en la base de datos')
                
    context = {**data}
    return render(request, 'registration/login.html', context)

def home_view(request):
    context = {}
    if request.user.is_authenticated:
        user_id = request.user.cvPersona_id
        persona = mPersona.objects.get(CvPersona=user_id)
        context['persona'] = persona
    
    return render(request, 'home.html', context)

def exit_view(request):
    logout(request)
    return redirect('home')

def user_list(request):
    user_data = User.objects.all()
    return render(request, 'user_list.html', {'user_data':user_data})

def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = CustomUserEditForm(instance=user)

    return render(request, 'user_edit.html', {'form': form})