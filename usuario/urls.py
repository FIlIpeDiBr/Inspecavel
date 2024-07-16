from django.urls import path
from django.contrib.auth import views as auth_views

from .views import IndexUserView, CadastrarUserView, ListarUserView, AlterarUserView


urlpatterns = [
    path('', IndexUserView.as_view(), name='users-index'),
    path('login/', auth_views.LoginView.as_view(
            template_name='paginas/autenticacao/form.html'
        ), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='users-logout'),
    path('cadastrar/', CadastrarUserView.as_view(), name='users-cadastrar'),
    path('listar-usuarios/', ListarUserView.as_view(), name='users-listar'),
    path('alterar/<int:pk>/', AlterarUserView.as_view(), name='users-alterar'),
]