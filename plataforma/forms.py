from django import forms
from .models import Pontos_turisticos

class Ponto_turistico_Form(forms.ModelForm):
    class Meta:
        model = Pontos_turisticos
        fields  = [
            'nome',
            'descricao',
            'endereco',
            'img',
            'img_capa',
            'funcionamento',
            'status',
            'categoria',
            'favorito',
            
        ]