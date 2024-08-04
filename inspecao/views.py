from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from inspecao.forms import InspecaoForm
from inspecao.models import Inspecao

class nova_inspecao(LoginRequiredMixin, CreateView):
    model = Inspecao
    form_class = InspecaoForm
    template_name = 'paginas/nova_inspecao.html'
    success_url = reverse_lazy('deteccao_monitor')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.moderador = self.request.user
        return super().form_valid(form)

    
class concluidas(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/concluidas.html'
    model = Inspecao
    context_object_name = 'inspecoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inspecao_1 = context['inspecoes'].filter(
            moderador=self.request.user,
            finalizada=True,
        )

        inspecao_2 = context['inspecoes'].filter(
            inspetores=self.request.user,
            discrepancia__discrepancia_filtrada__severidade__isnull=False)
        
        context['inspecoes_moderador'] = inspecao_1
        context['inspecoes_inspetor'] = inspecao_2

        return context


class em_aberto(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/em_aberto.html'
    model = Inspecao
    context_object_name = 'inspecoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inspecao_1 = context['inspecoes'].filter(
            moderador=self.request.user,
            finalizada=False,
        )

        inspecao_2 = context['inspecoes'].filter(
            inspetores=self.request.user,
            discrepancia__discrepancia_filtrada__severidade__isnull=True)
        
        context['inspecoes_moderador'] = inspecao_1
        context['inspecoes_inspetor'] = inspecao_2

        return context
