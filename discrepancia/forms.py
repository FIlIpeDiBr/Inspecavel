from django import forms
from discrepancia.models import Discrepancia

class DiscrepanciaForm(forms.ModelForm):
    class Meta:
        model = Discrepancia
        fields= [
            "descricao",
            "localizacao_geral",
            "localizacao_especifica",
            "tipo",
            #"fonte",
        ]

    # def __init__(self, *args, **kwargs):
    #     inspecao_id = kwargs.pop('inspecao', None)
    #     super().__init__(*args, **kwargs)
    #     if inspecao_id:
    #         self.instance.inspecao_id = inspecao_id