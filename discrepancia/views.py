from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class colecao_inspetor(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'colecao_inspetor.html'