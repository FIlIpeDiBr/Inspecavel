from django.contrib import admin
from django.urls import path, include

from discrepancia.views import deteccao_inspetor, deteccao_monitor, colecao, discriminacao

urlpatterns = [
    path('', include('inspecao.urls')),
    path('deteccao/inspetor', deteccao_inspetor.as_view(), name='deteccao_inspetor'),
    path('deteccao/monitor', deteccao_monitor.as_view(), name='deteccao_monitor'),
    path('colecao', colecao.as_view(), name='colecao'),
    path('colecao', colecao.as_view(), name='colecao'),
    path('discriminacao', discriminacao.as_view(), name='discriminacao'),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
]
