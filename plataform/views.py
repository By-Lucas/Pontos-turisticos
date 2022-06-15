# from django.shortcuts import render

# # Create your views here.

from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.forms import AuthenticationForm
from .models import Places_visits, image_slider_place
from .forms import Place_visit_Form, ImagesSliderForm
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
    p_visits = Places_visits.objects.all()
    user = request.user
    print(user)

    context ={
        'p_visits':p_visits,
        'user':user
    }
    return render(request, 'index.html', context)

# Add image slider
def add_image_slider(request):
    all_img =  image_slider_place.objects.all()
    form = ImagesSliderForm(request.POST, request.FILES)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Image add!')
            return redirect('add-image')
        else:
            messages.add_message(request, constants.ERROR, 'Erro New image!')
            return redirect(request, 'add-image')
    context = {
        'form':form,
        'all_img':all_img
    }
    return render(request, 'regist/add-image.html',context)


@login_required
def register_place_visit(request):
    form = Place_visit_Form(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'New Place Sucess Register!')
            return redirect('index')
        else:
            messages.add_message(request, constants.ERROR, 'Erro New Place Register!')
            return redirect(request, 'register_places')
    context = {
        'form':form
    }
    return render(request, 'regist/register_places.html', context)


@login_required
def delete_place_visit(request, id=None):
    place_remove = get_object_or_404(Places_visits, id=id)
    if request.method == "POST": 
        place_remove.delete()
        messages.add_message(request, constants.SUCCESS, "Place Success Removed") #client removed
        return redirect('index')
    return render(request, 'regist/delete_place_visit.html',{'place_remove':place_remove})

class TurismUpdateView(TemplateView):
    template_name = 'regist/edit_place_visit.html'

    # load Place Visit INFO 
    def get(self, request, id=None):
        project_ = get_object_or_404(Places_visits, id=id)
        form = Place_visit_Form(instance=project_)
        # WHAT IS INSIDE OF CONTEXT CAN BE USED ON TAMPLATE
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    # SALVE EDITED INFORMATION DIRECTLY IN THE DATABASE
    def post(self, request, id=None):
        project_ = get_object_or_404(Places_visits, id=id)
        print(project_)
        form = Place_visit_Form(request.POST, request.FILES, instance=project_)
        if  form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, "Place visit edited Successfully")
            return redirect(reverse_lazy('index'))
        else:
            messages.add_message(request, constants.ERROR, "Error editing Place to Visit")
            return redirect(reverse_lazy('index'))
        return self.render_to_response(context)

def place_visit_(request, id):
    place_visit = get_object_or_404(Places_visits, id=id)

    #SUGGESTIONS FOR THE USER, JUST CHANGE(category=place_visit.category) for (status=place_visit.status)
    #TO SHOW RANDOMLY
    sugestions = Places_visits.objects.filter(category=place_visit.category).exclude(id=id)[:4]
    context ={
        'place_visit': place_visit, 
        'sugestions': sugestions, 
        'id': id
    }
    return render(request, 'place_visit_id.html', context)