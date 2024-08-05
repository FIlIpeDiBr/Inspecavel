from django import forms
from discrepancia.models import Discrepancia
from artefato.models import Artefato
from discrepancia_filtrada.models import Discrepancia_filtrada

class DiscrepanciaForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=[])
    class Meta:
        model = Discrepancia
        fields= [
            "descricao",
            "localizacao_geral",
            "localizacao_especifica",
            "tipo",
            #"fonte",
        ]

    def __init__(self, *args, **kwargs):
        artefato_id = kwargs.pop('artefato_id', None)
        super().__init__(*args, **kwargs)

        if artefato_id:
            # Obter o artefato e definir as opções do campo tipo
            try:
                artefato = Artefato.objects.get(id=artefato_id)
                tipos = artefato.tipo_defeito.split(';')
                self.fields['tipo'].choices = [(tipo, tipo) for tipo in tipos]
            except Artefato.DoesNotExist:
                self.fields['tipo'].choices = []

    # def __init__(self, *args, **kwargs):
    #     inspecao_id = kwargs.pop('inspecao', None)
    #     super().__init__(*args, **kwargs)
    #     if inspecao_id:
    #         self.instance.inspecao_id = inspecao_id

class DiscrepanciaFiltradaInlineForm(forms.ModelForm):
    class Meta:
        model = Discrepancia_filtrada
        fields = ['severidade']

    def __init__(self, *args, **kwargs):
        artefato_id = kwargs.pop('artefato_id', None)
        super().__init__(*args, **kwargs)

        if artefato_id:
            try:
                artefato = Artefato.objects.get(id=artefato_id)
                severidades = artefato.lista_severidade.split(';')
                self.fields['severidade'].widget = forms.Select(choices=[(s, s) for s in severidades])
            except Artefato.DoesNotExist:
                self.fields['severidade'].widget = forms.Select(choices=[])
