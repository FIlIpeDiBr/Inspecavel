from django.urls import path

from inspecao.views import concluidas, em_aberto, nova_inspecao


urlpatterns = [
    path('', em_aberto.as_view(), name='em_aberto'),
    path('concluidas', concluidas.as_view(), name='concluidas'),
    path('nova_inspecao', nova_inspecao.as_view(), name='nova_inspecao'),
]