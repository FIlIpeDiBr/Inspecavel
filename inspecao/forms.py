from django import forms
from inspecao.models import Inspecao


class InspecaoForm(forms.ModelForm):
    class Meta:
        model = Inspecao
        fields = [
            "titulo",
            "inspetores",
            "artefato",
            "link",
            "data_limite"
        ]
        widgets = {
            'data_limite': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'teste'}),
        }