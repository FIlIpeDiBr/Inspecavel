from django.db import models
from usuario.models import User
from artefato.models import Artefato


class Inspecao(models.Model):
    titulo = models.CharField("Título", max_length=50, unique=True)
    moderador = models.ForeignKey(User, on_delete=models.PROTECT)
    inspetores = models.ManyToManyField(User, related_name='inspetores')
    artefato = models.OneToOneField(Artefato, on_delete=models.PROTECT)
    link = models.URLField()
    data_limite = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    finalizada = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Inspeção"
        verbose_name_plural = "Inspeções"

    def __str__(self) -> str:
        return self.titulo
