from django.db import models
from discrepancia.models import Discrepancia

class Discrepancia_filtrada(models.Model):
    principal = models.OneToOneField(Discrepancia, verbose_name='Discrepância principal', on_delete=models.CASCADE)
    repetidas = models.ManyToManyField(Discrepancia, related_name='discrepancias_repetidas',blank=True)
    severidade = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = "Discrepância filtrada"
        verbose_name_plural = "Discrepâncias filtradas"

    def __str__(self) -> str:
        return str(self.principal)
