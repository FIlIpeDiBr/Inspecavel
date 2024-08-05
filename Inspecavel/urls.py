from django.contrib import admin
from django.urls import path, include

from discrepancia.views import deteccao_inspetor, deteccao_monitor, colecao, colecao_agrupar, discriminacao, exportar_dados
from artefato.views import novo_artefato

urlpatterns = [
    path('', include('inspecao.urls')),

    path('deteccao/inspetor/<int:pk>', deteccao_inspetor.as_view(), name='deteccao_inspetor'),
    path('deteccao/monitor/<int:pk>', deteccao_monitor.as_view(), name='deteccao_monitor'),
    path('colecao', colecao.as_view(), name='colecao'),
    path('colecao/agrupar/<int:pk>', colecao_agrupar.as_view(), name='colecao_agrupar'),
    path('discriminacao', discriminacao.as_view(), name='discriminacao'),
    path('exportar/', exportar_dados, name="exportar"),

    path('novo/artefato', novo_artefato.as_view(), name="novo_artefato"),


    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
]
