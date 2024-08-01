from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from inspecao.models import Inspecao


class concluidas(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/concluidas.html'
    model = Inspecao
    context_object_name = 'inspecoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inspecao_1 = context['inspecoes'].filter(
            moderador=self.request.user, discrepancia__discrepancia_filtrada__severidade__isnull=False)
        inspecao_2 = context['inspecoes'].filter(
            inspetores=self.request.user,  discrepancia__discrepancia_filtrada__severidade__isnull=False)
        
        context['inspecoes_moderador'] = inspecao_1
        context['inspecoes_inspetor'] = inspecao_2

        return context


class em_aberto(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/em_aberto.html'
