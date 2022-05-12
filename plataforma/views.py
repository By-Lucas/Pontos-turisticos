from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.forms import AuthenticationForm
from .models import Pontos_turisticos
from .forms import Ponto_turistico_Form
from users.models import Profile


class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    next_page = 'profile'
    def get(self, request):
        return render(request, self.template_name, {'form': AuthenticationForm})

class LogoutView(auth_views.LogoutView):
    next_page = 'login'

def index(request):
    perfil = Profile.objects.all()
    p_turisticos = Pontos_turisticos.objects.all()
    usuario = request.user
    print(usuario)

    context ={
        'p_turisticos':p_turisticos,
        'usuario':usuario
    }
    return render(request, 'index.html', context)

@login_required
def cadastrar_ponto_turistico(request):
    form = Ponto_turistico_Form(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Ponto turistico cadastrado com sucesso!')
            return redirect(request, 'index')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar Ponto turistico!')
            return redirect(request, 'cadastrar_pontos')
    context = {
        'form':form
    }
    return render(request, 'cadastro/cadastrar_pontos.html', context)


@login_required
def deletar_ponto_turistico(request, id=None):
    ponto_remover = get_object_or_404(Pontos_turisticos, id=id)
    if request.method == "POST": 
        ponto_remover.delete()
        messages.add_message(request, constants.SUCCESS, "Ponto turistico deletado com sucesso") #cliente removido
        return redirect('index')
    return render(request, 'cadastro/deletar_ponto_turistico.html',{'ponto_remover':ponto_remover})

@login_required
def editar_ponto_turistico(request, id=None):
    projeto_ = get_object_or_404(Pontos_turisticos, id=id)
    form = Ponto_turistico_Form(request.POST or None, instance=projeto_)
    if request.method == 'POST':
        if  form.is_valid():
            obj = form.save()
            obj.save()
            messages.add_message(request, constants.SUCCESS, "Ponto turistico editado com sucesso")
            return redirect('index')
        else:
            messages.add_message(request, constants.ERROR, "Erro ao editar Ponto turistico")
            return redirect('index')
    return render(request, 'cadastro/editar_ponto_turistico.html', {'form':form})
