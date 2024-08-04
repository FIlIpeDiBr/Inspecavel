from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from artefato.forms import ArtefatoForm
from artefato.models import Artefato

class novo_artefato(LoginRequiredMixin, CreateView):
    model = Artefato
    form_class = ArtefatoForm
    template_name = 'novo_artefato.html'
    success_url = reverse_lazy('users-login')
    
