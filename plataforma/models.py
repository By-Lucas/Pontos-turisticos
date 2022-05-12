from distutils.command.upload import upload
from sre_constants import CATEGORY
from django.db import models

class imagem_slider_ponto(models.Model):
    imagens = models.ImageField(upload_to='pontos-turisticos/', null=True, blank=True)
    def __str__(self) -> str:
        return self.imagens.url  

# Create your models here.
class Pontos_turisticos(models.Model):
    STATUS_CHOICE = (
        ('A','Aberto'),
        ('B','Fechado'),
        ('R', 'Reforma'),
    )
    CATEGORIA_CHOICE = (
        ('I', 'Infantil'),
        ('A', 'Adulto'),
        ('V', 'Idoso')
    )
    nome = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    img = models.ManyToManyField(imagem_slider_ponto, null=True, blank=True)
    img_capa = models.ImageField(upload_to='pontos-turisticos/capa', null=True, blank=True)
    funcionamento = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE,  null=True, blank=True)
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICE, null=True, blank=True)
    favorito = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.nome