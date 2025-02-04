from django.db import models
from django.utils import timezone
from usuario.models import User
from artefato.models import Artefato


class Inspecao(models.Model):
    titulo = models.CharField("Título", max_length=50, unique=True)
    moderador = models.ForeignKey(User, on_delete=models.PROTECT)
    inspetores = models.ManyToManyField(User, related_name='inspetores')
    artefato = models.ForeignKey(Artefato, on_delete=models.PROTECT)
    link = models.URLField(blank=True)
    data_limite = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deteccao_finalizada = models.BooleanField(default=False)
    deteccao_finalizada_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    colecao_finalizada = models.BooleanField(default=False)
    inspecao_finalizada = models.BooleanField(default=False)
    inspecao_finalizada_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    inspecao_cancelada = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Inspeção"
        verbose_name_plural = "Inspeções"

    def __str__(self) -> str:
        return self.titulo
