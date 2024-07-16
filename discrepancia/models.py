from django.db import models
from inspetor.models import Inspetor
from inspecao.models import Inspecao


class Discrepancia(models.Model):
    responsavel = models.ForeignKey(Inspetor, verbose_name='Responsável', on_delete=models.PROTECT)
    fonte = models.ForeignKey(Inspecao, on_delete=models.PROTECT)
    descricao = models.TextField(verbose_name='Descrição', max_length=100)
    localizacao = models.CharField(verbose_name='Localização', max_length=50)
    tipo = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Discrepância"
        verbose_name_plural = "Discrepâncias"

    def __str__(self) -> str:
        return f'{self.fonte} - {self.tipo} - {self.localizacao}'
