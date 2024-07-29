from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from .forms import UserChangeForm, UserCreationForm
from .models import User


class IndexUserView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/users/index.html'


class CadastrarUserView(CreateView):
    template_name = 'paginas/users/form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('users-listar')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Usuário'
        context['tipo_operacao'] = 'cadastro'

        return context


class AlterarUserView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/users/form.html'
    form_class = UserChangeForm
    model = User
    success_url = reverse_lazy('users-listar')

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user != request.user:
            return HttpResponseForbidden("<h1>Você não tem permissão para editar os dados deste usuário. Saifora!!!</h1>")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        login_url = reverse_lazy('users-login')
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Alterar Usuário'
        context['tipo_operacao'] = 'alterar'

        return context


class ListarUserView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    template_name = 'paginas/users/list.html'
    model = User
    paginate_by = 5
