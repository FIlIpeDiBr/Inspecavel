from django import forms
from inspecao.models import Artefato


class ArtefatoForm(forms.ModelForm):
    class Meta:
        model = Artefato
        fields = [
                "titulo",
                "nomeclatura_geral",
                "formato_geral",
                "nomeclatura_espcifica",
                "formato_especifico",
                "tipo_defeito",
                "lista_severidade"
            ]