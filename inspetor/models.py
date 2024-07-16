from django.db import models
from inspecao.models import Inspecao
from usuario.models import User


class Inspetor(models.Model):
    inspecao = models.ForeignKey(Inspecao, verbose_name='Inspeção', on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.inspecao} - {self.usuario}'
