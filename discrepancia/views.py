import io
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, TemplateView, ListView, CreateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Count

from discrepancia.forms import DiscrepanciaForm
from discrepancia.models import Discrepancia

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, TableStyle, LongTable, SimpleDocTemplate, Spacer

from inspecao.models import Inspecao
from artefato.models import Artefato
from discrepancia_filtrada.models import Discrepancia_filtrada
from artefato.models import Artefato
from discrepancia_filtrada.models import Discrepancia_filtrada
from artefato.models import Artefato
from discrepancia.forms import DiscrepanciaFiltradaInlineForm


class deteccao_inspetor(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users-login')
    template_name = 'deteccao_inspetor.html'
    form_class = DiscrepanciaForm
    model = Discrepancia

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        artefato_id = Inspecao.objects.get(pk=self.kwargs['pk']).artefato.id
        kwargs['artefato_id'] = artefato_id
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

# Mano, desculpa mesmo
        inspecao = Inspecao.objects.filter(pk=self.kwargs['pk']).values('artefato', 'titulo')
        context['nomenclatura_especifica'] = Artefato.objects.filter(pk = inspecao[0]['artefato']).values('nomeclatura_espcifica').distinct().values()[0]['nomeclatura_espcifica']
        context['nomenclatura_geral'] = Artefato.objects.filter(pk = inspecao[0]['artefato']).values('nomeclatura_geral').distinct().values()[0]['nomeclatura_geral']
        
        context['titulo_inspecao'] = inspecao[0]['titulo']

        return context

    def get_success_url(self):
        # Redireciona para a página de inspeção ou outra página após salvar
        return reverse_lazy('deteccao_inspetor', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.responsavel = self.request.user
        form.instance.fonte = get_object_or_404(Inspecao, pk=self.kwargs['pk'])
        return super().form_valid(form)

class deteccao_monitor(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    model = Inspecao
    template_name = 'deteccao_monitor.html'
    context_object_name = 'inspetores'

    def get_queryset(self):
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        query = Discrepancia.objects.filter(fonte=inspecao).values('responsavel__username').annotate(total=Count('id'))
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        soma_discrepancias = Discrepancia.objects.filter(fonte=inspecao).count()
        
        context['inspecao'] = inspecao
        context['soma_discrepancias'] = soma_discrepancias
        return context

    def post(self, request, *args, **kwargs):
        if 'concluir_deteccao' in request.POST:
            return self.concluir_deteccao(request)
        return redirect('concluidas')

    def concluir_deteccao(self, request):
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        inspecao.deteccao_finalizada = True
        inspecao.save()
        return redirect('concluidas')
    

class colecao(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    model = Discrepancia
    template_name = 'colecao.html'
    context_object_name = 'discrepancias'

    def get_queryset(self):
        # Filtrar para exibir apenas as discrepâncias que não foram agrupadas
        return Discrepancia.objects.exclude(id__in=Discrepancia_filtrada.objects.values('principal_id')).exclude(id__in=Discrepancia_filtrada.objects.values('repetidas')).filter(fonte=Inspecao.objects.get(pk=self.kwargs['pk']))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

# Mano, desculpa mesmo
        inspecao = Inspecao.objects.filter(pk=self.kwargs['pk']).values('artefato', 'titulo')
        context['nomenclatura_especifica'] = Artefato.objects.filter(pk = inspecao[0]['artefato']).values('nomeclatura_espcifica').distinct().values()[0]['nomeclatura_espcifica']
        context['nomenclatura_geral'] = Artefato.objects.filter(pk = inspecao[0]['artefato']).values('nomeclatura_geral').distinct().values()[0]['nomeclatura_geral']
        
        context['titulo_inspecao'] = inspecao[0]['titulo']

        return context


class colecao_agrupar(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users-login')
    model = Discrepancia_filtrada
    template_name = 'colecao_agrupar.html'
    fields = ['repetidas']
    success_url = reverse_lazy('colecao')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        discrepancia_principal = get_object_or_404(Discrepancia, pk=self.kwargs.get('pk'))

        # Filtrar para que a discrepância principal e as já agrupadas não apareçam na lista de repetidas
        form.fields['repetidas'].queryset = Discrepancia.objects.exclude(
            pk=discrepancia_principal.pk
        ).exclude(
            id__in=Discrepancia_filtrada.objects.values('repetidas')
        ).filter(fonte=Inspecao.objects.get(pk=self.kwargs['pk']))

        return form

    def form_valid(self, form):
        discrepancia_principal = get_object_or_404(Discrepancia, pk=self.kwargs.get('pk'))
        
        # Atribuir a instância de Discrepancia ao campo principal
        form.instance.principal = discrepancia_principal
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    fields = ['repetidas']
    success_url = reverse_lazy('colecao')


class discriminacao(LoginRequiredMixin, View):
    login_url = reverse_lazy('users-login')
    template_name = 'discriminacao.html'
    # success_url = reverse_lazy('colecao')  # Redirecione para onde você desejar após o sucesso

    def get(self, request, *args, **kwargs):
        return self.render_formsets(request)

    def post(self, request, *args, **kwargs):
        if 'concluir_inspecao' in request.POST:
            return self.concluir_inspecao(request)
        else:
            return self.salvar_alteracoes(request)

    def salvar_alteracoes(self, request):
        discrepancias = Discrepancia.objects.filter(fonte=Inspecao.objects.get(pk=self.kwargs['pk']))
        all_forms_valid = True

        for discrepancia in discrepancias:
            artefato_id = discrepancia.fonte.artefato.id if discrepancia.fonte else None
            form = DiscrepanciaFiltradaInlineForm(
                request.POST, 
                instance=Discrepancia_filtrada.objects.get(principal=discrepancia),
                artefato_id=artefato_id,
                prefix=f'discrepancia_{discrepancia.id}'
            )
            if form.is_valid():
                form.save()
            else:
                all_forms_valid = False

        if all_forms_valid:
            return self.render_formsets(request)
        else:
            return self.render_formsets(request, request.POST)

    def concluir_inspecao(self, request):
        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])
        inspecao.inspecao_finalizada = True
        inspecao.save()
        return redirect('concluidas')  # Redirecione para a URL desejada após concluir a inspeção

    def render_formsets(self, request, post_data=None):
        discrepancias = Discrepancia.objects.filter(fonte=Inspecao.objects.get(pk=self.kwargs['pk']))
        formsets = []

        for discrepancia in discrepancias:
            filtrada, created = Discrepancia_filtrada.objects.get_or_create(principal=discrepancia)
            artefato_id = discrepancia.fonte.artefato.id if discrepancia.fonte else None
            form = DiscrepanciaFiltradaInlineForm(
                post_data, 
                instance=filtrada, 
                artefato_id=artefato_id,
                prefix=f'discrepancia_{discrepancia.id}'
            )
            formsets.append((discrepancia, form))

        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])
        titulo_inspecao = inspecao.titulo

        return render(request, self.template_name, {'formsets': formsets, 'titulo_inspecao': titulo_inspecao})


@login_required
def exportar_dados(request, pk):
    inspec = Inspecao.objects.get(pk=pk)
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)

    elements = []

    style_header = ParagraphStyle(
        'header',
        fontSize=12,
        alignment=1,
        fontName='Helvetica-Bold',
    )

    style_cels = ParagraphStyle(
        'cels',
        fontSize=11
    )

    elements = [Paragraph(f'Título: {inspec.titulo}', style_header)]
    
    elements.append(Spacer(1, 20))

    discrepancias = Discrepancia_filtrada.objects.all()
    
    data = [['Localiza', 'Descrição', 'Autor', 'Tipo', 'Severidade']]

    for discrepancia in discrepancias:
        localizacao = discrepancia.principal.localizacao_geral
        descricao = discrepancia.principal.descricao
        autor = discrepancia.principal.responsavel
        tipo = discrepancia.principal.tipo
        severidade = discrepancia.severidade
        data.append([
            localizacao,
            Paragraph(descricao, style_cels),
            autor,
            tipo,
            severidade
        ])

    table = LongTable(data, colWidths=[80, '*', 80, 80, 80])
    elements.append(table)
    elements.append(Spacer(1, 20))

    table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

    doc.build(elements)
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='relatorio.pdf')