from base.forms import CustomUserCreation, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.utils import timezone
from user.models import mPersona, User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_creation_form = CustomUserCreation(request.POST)

            if user_creation_form.is_valid():
                user = user_creation_form.save()  # Guarda el nuevo usuario
                login(request, user)  # Inicia sesión al nuevo usuario
                return redirect('home')  # Redirige a la página de inicio después de registrarse

        else:
            user_creation_form = CustomUserCreation()
    else:
        return redirect('login')
    context = {'form': user_creation_form}
    return render(request, 'registration/register.html', context)


def login_view(request):
    data= {
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
                userA =  User.objects.get(id=user_id.id)

                now = timezone.now()
                if userA.dateEnd is not None:

                    if (now > userA.dateEnd or userA.date_joined>now):
                        userA.is_active = False
                    else:
                        userA.is_active = True
                userA.save()

                if userA.is_active:
                    if user is not None:        
                        login(request, user)  
                        return redirect('home') 
                    else:
                        messages.error(request, 'Credenciales de inicio de sesión incorrectas.')
                else:
                    messages.error(request, 'Su cuenta está desactivada. Póngase en contacto con el administrador.')
            except ObjectDoesNotExist:
                messages.error(request, 'El usuario no existe en la base de datos')
                
    context = {**data}
    return render(request, 'registration/login.html', context)

def home(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        persona = mPersona.objects.get(CvPersona=user_id)
        context = {'persona': persona}
    else:
        context={}
    
    return render(request, 'home.html', context)

def exit(request):
    logout(request)
    return redirect('home')
