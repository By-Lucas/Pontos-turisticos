from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.forms import AuthenticationForm
from .models import Pontos_turisticos
from users.models import Profile


class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    next_page = 'profile'
    def get(self, request):
        return render(request, self.template_name, {'form': AuthenticationForm})

class LogoutView(auth_views.LogoutView):
    next_page = 'login'

def index(request):
    #all_pontos = get_object_or_404(Pontos_turisticos)
    
    perfil = Profile.objects.all()
    p_turisticos = Pontos_turisticos.objects.all()

    usuario = request.user
    print(usuario)


    context ={
        #'sugestoes': sugestoes,
        'p_turisticos':p_turisticos,
        'usuario':usuario
    }
    return render(request, 'index.html', context)
