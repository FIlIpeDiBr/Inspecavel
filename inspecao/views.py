from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class concluidas(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/concluidas.html'

class em_aberto(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/em_aberto.html'