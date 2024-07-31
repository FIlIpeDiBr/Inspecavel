"""
URL configuration for Inspecavel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from inspecao.views import concluidas, em_aberto
from discrepancia.views import deteccao_inspetor, deteccao_monitor, colecao

urlpatterns = [
    path('', concluidas.as_view(), name='concluidas'),
    path('em_aberto', em_aberto.as_view(), name='em_aberto'),
    path('deteccao/inspetor', deteccao_inspetor.as_view(), name='deteccao_inspetor'),
    path('deteccao/monitor', deteccao_monitor.as_view(), name='deteccao_monitor'),
    path('colecao', colecao.as_view(), name='colecao'),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
]
