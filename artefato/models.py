from django.db import models


class Artefato(models.Model):
    titulo = models.CharField('Título', max_length=50)
    nomeclatura_geral = models.CharField('Nomeclatura geral', max_length=30)
    formato_geral = models.BooleanField('O formato geral permite letras?', default=True)
    nomeclatura_espcifica = models.CharField('Nomeclatura específica', max_length=20, blank=True) #tá escrito errado especifica kkkkkkkkkk
    formato_especifico = models.BooleanField('O formato específico permite letras?', blank=True)
    tipo_defeito = models.CharField('Tipos de defeito',max_length=200)
    lista_severidade = models.CharField('Graus de severidade', max_length=200)

    def __str__(self):
        return self.titulo