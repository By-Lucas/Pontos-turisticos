from django import forms
from .models import Places_visits, image_slider_place

class Place_visit_Form(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True,  widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'name here'}))
    address = forms.CharField(max_length=30, required=True,  widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'address here'}))
    description_place = forms.CharField(max_length=500, required=True,  widget=forms.Textarea(attrs={"class": "textarea is-success is-medium",'placeholder': 'description here '}))

    class Meta: 
        model = Places_visits
        fields  = [
            'name',
            'description_place',
            'address',
            'img',
            'img_cover',
            'operation',
            'status',
            'category',
            'favorite',
        ]

class ImagesSliderForm(forms.ModelForm):
    class Meta:
        model=image_slider_place
        fields = ('images',)
