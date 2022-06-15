from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# ABAIXO FICA TODO OS FORMULARIO PUXADO DA models, E ISSO É RENDERIZADO NO HTML ATRAVEZ DA VIEWS


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

        error_messagens = {
            "username": {
                "required": "Enter the username."
            },
            "first_name": {
                "required": "Enter the last name."
            },
            "last_name": {
                "required": "Enter the last name."
            },
            "email": {
                "required": "Enter the email."
            },
            "password1": {
                "required": "Enter the password."
            },
            "password2": {
                "required": "confirm password."
            },

        }

class ProfileForm(forms.ModelForm):
    DOB = forms.DateField(required=False, widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Date 0000/00/00'
            }
        ))
    class Meta:
        model = Profile
        fields = [
            'age',
            'city',
            'address',
            'contact',
            'DOB',
            'image_profile',
            #'data_cadastro'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['DOB'].widget = forms.DateInput(format="%d/%m/%Y")
