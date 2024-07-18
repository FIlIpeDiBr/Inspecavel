from django.db import models


class Artefato(models.Model):
    titulo = models.CharField('Título', max_length=50)
    nomeclatura_geral = models.CharField('Nomeclatura geral', max_length=30)
    formato_geral = models.CharField(max_length=20)
    nomeclatura_espcifica = models.CharField('Nomeclatura específica', max_length=20)
    formato_especifico = models.CharField('Formato específico', max_length=20)
    tipo_defeito = models.CharField(max_length=100)
    lista_severidade = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo