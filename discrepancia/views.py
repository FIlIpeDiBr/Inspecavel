from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class deteccao_inspetor(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'deteccao_inspetor.html'
    success_url = reverse_lazy('users-login')

    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super().form_valid(form)

class deteccao_monitor(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'deteccao_monitor.html'

class colecao(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'colecao.html'

class colecao_agrupar(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'colecao_agrupar.html'

class discriminacao(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'discriminacao.html'