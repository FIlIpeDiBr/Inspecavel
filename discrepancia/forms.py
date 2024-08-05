from django import forms
from discrepancia.models import Discrepancia

class DiscrepanciaForm():
    class Meta:
        model = Discrepancia
        fields= [
            "descricao",
            "localizacao_geral",
            "localizacao_especifica",
            "tipo"
        ]