from django.db import models
from usuario.models import User
from inspecao.models import Inspecao


class Discrepancia(models.Model):
    responsavel = models.ForeignKey(User, verbose_name='Responsável', on_delete=models.CASCADE)
    fonte = models.ForeignKey(Inspecao, on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name='Descrição', max_length=160)
    localizacao_geral = models.CharField(verbose_name='Localização Geral', max_length=20)
    localizacao_especifica = models.CharField(verbose_name='Localização Específica', max_length=20)
    tipo = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Discrepância"
        verbose_name_plural = "Discrepâncias"

    def __str__(self) -> str:
        return f'{self.descricao} - {self.tipo}'
