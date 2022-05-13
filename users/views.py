# CARREGAR OS MODULOS DO DJANGO 
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

# BUSCA O FORMUARIO DO DJANGO
from .forms import UserForm, ProfileForm, SignUpForm

### AQUI NA VIEWS FICA TODA A CONEXÃO ENTRE O BANCO DE DADOS(models) E TEMPLATES(html) ###


#VIEW DO PERFIL
class profileView(TemplateView):
    template_name = 'profile.html' #TEMPLATE QUE É RENDERIZADO PRA ESTA CLASS EM TODAS AS CLASS E VIEWS

    def get(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        #O QUE FICA DENTRO DO CONTEXT PODE SER USADO NO TEMPLATE
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

# ATUALIZAR PERFIL
class ProfileUpdateView(TemplateView):
    template_name = 'profile-edit.html'

    # CARREGAR INFO DO PERFIL
    def get(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        #O QUE FICA DENTRO DO CONTEXT PODE SER USADO NO TEMPLATE
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

    #SALVAR EDICOES DO PERFIL CASO O FORMULARIO SEJA VALIDO
    def post(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid(): #VERIFICA SE O FORMULARIO É VALIDO E SE FOR SERÁ SALVO
            user_form.save()
            profile_form.save()
            messages.add_message(request, constants.SUCCESS, 'Perfil editado com sucesso!')
            return redirect(reverse_lazy('profile')) #AQUI É A PAGINA PRA ONDE O USUARIO VAI SER DIRECIONADO
        context = {
            'user_form':user_form,
            'profile_form':profile_form
        }
        return self.render_to_response(context)

# FAZER LOGIN 
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'register.html'

# ALTERAR SENHA
class PasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('redirect')
    template_name = 'password/password-change.html'

#RESETAR SENHA
class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'password/password-reset-form.html'
    subject_template_name = 'password/password-reset-subject.txt'
    email_template_name = 'password/password-reset-email.html'

#PAGINA DE CONCLUSAO SOBRE A ALTERAÇÃO DA SENHA
class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'password/password-reset-done.html'

#CONFIRMAÇÃO DE ALTERAÇÃO DE SENHA
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password/password-reset-confirm.html'

#RESET DE SENHA CONCLUIDO
class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'password/password-reset-complete.html'