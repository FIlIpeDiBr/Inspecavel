from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from artefato.models import Artefato

class novo_artefato(LoginRequiredMixin, CreateView):
    model = Artefato
    template_name = 'novo_artefato.html'
    success_url = reverse_lazy('users-login')
    fields = [
        "titulo",
        "nomeclatura_geral",
        "formato_geral",
        "nomeclatura_espcifica",
        "formato_especifico",
        "tipo_defeito",
        "lista_severidade"
    ]
