from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants


def index(request):
    return render(request, 'index.html')
