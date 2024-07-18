from django.db import models
from discrepancia.models import Discrepancia

class Discrepancia_filtrada(models.Model):
    principal = models.OneToOneField(Discrepancia, verbose_name='Discrepância principal,', on_delete=models.PROTECT)
    repetidas = models.ManyToManyField(Discrepancia, on_delete=models.PROTECT)
    severidade = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Discrepância filtrada"
        verbose_name_plural = "Discrepâncias filtradas"

    def __str__(self) -> str:
        return self.principal
