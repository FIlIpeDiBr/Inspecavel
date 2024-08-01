from django.urls import path

from inspecao.views import concluidas, em_aberto


urlpatterns = [
    path('', concluidas.as_view(), name='concluidas'),
    path('em_aberto', em_aberto.as_view(), name='em_aberto'),
]