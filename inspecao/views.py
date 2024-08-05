from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from inspecao.forms import InspecaoForm
from inspecao.models import Inspecao

class nova_inspecao(LoginRequiredMixin, CreateView):
    model = Inspecao
    form_class = InspecaoForm
    template_name = 'paginas/nova_inspecao.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.moderador = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('deteccao_monitor', kwargs={'pk': self.object.pk})

    
class concluidas(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/concluidas.html'
    model = Inspecao
    context_object_name = 'inspecoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['inspecoes_moderador'] = context['inspecoes'].filter(
            moderador=self.request.user,
            inspecao_finalizada=True,
        )

        context['inspecoes_inspetor'] = context['inspecoes'].filter(
            inspetores=self.request.user,
            deteccao_finalizada=True)
                
        return context


class em_aberto(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/em_aberto.html'
    model = Inspecao
    context_object_name = 'inspecoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        c_moderador = context['inspecoes'].filter(
            moderador=self.request.user,
            inspecao_finalizada=False,
        )

        c_inspetor = context['inspecoes'].filter(
            inspetores=self.request.user,
            deteccao_finalizada=False)
        
        context['inspecoes_moderador'] = c_moderador
        context['inspecoes_inspetor'] = c_inspetor

        return context
