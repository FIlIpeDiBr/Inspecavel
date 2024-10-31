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
            'data_limite': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['inspetores'].queryset = self.fields['inspetores'].queryset.exclude(id=user.id)
