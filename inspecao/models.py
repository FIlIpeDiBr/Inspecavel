from django.db import models
from usuario.models import User


class Inspecao(models.Model):
    titulo = models.CharField("Título", max_length=50, unique=True)
    moderador = models.ForeignKey(User, on_delete=models.PROTECT)
    inspetores = models.ManyToManyField(User, related_name='inspetores')
    artefato = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Inspeção"
        verbose_name_plural = "Inspeções"

    def __str__(self) -> str:
        return self.titulo
