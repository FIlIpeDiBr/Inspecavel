import io
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Count
from django.contrib import messages
from django.utils.timezone import now


from discrepancia.forms import DiscrepanciaForm
from discrepancia.models import Discrepancia

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, TableStyle, LongTable, SimpleDocTemplate, Spacer

from inspecao.models import Inspecao
from discrepancia_filtrada.models import Discrepancia_filtrada
from artefato.models import Artefato
from discrepancia.forms import DiscrepanciaFiltradaInlineForm

class deteccao_inspetor(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users-login')
    template_name = 'deteccao_inspetor.html'
    form_class = DiscrepanciaForm
    model = Discrepancia

    def dispatch(self, request, *args, **kwargs):
        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])

        if inspecao.deteccao_finalizada:
            messages.error(request, "Acesso negado. A detecção já foi finalizada.")
            return redirect(request.META.get('HTTP_REFERER', 'em_aberto'))
        
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        artefato_id = Inspecao.objects.get(pk=self.kwargs['pk']).artefato.id
        kwargs['artefato_id'] = artefato_id
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inspecao = Inspecao.objects.filter(pk=self.kwargs['pk']).values('artefato', 'titulo').first()

        context['nomenclatura_especifica'] = Artefato.objects.filter(pk = inspecao['artefato']
            ).values('nomeclatura_espcifica').first()['nomeclatura_espcifica']
        
        context['nomenclatura_geral'] = Artefato.objects.filter(pk = inspecao['artefato']
            ).values('nomeclatura_geral').first()['nomeclatura_geral']
        
        context['titulo_inspecao'] = inspecao['titulo']

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

    def dispatch(self, request, *args, **kwargs):
        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])

        if inspecao.deteccao_finalizada:
            messages.error(request, "Acesso negado. A detecção já foi finalizada.")
            return redirect(request.META.get('HTTP_REFERER', 'em_aberto'))
        
        return super().dispatch(request, *args, **kwargs)

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
        
        elif 'cancelar_inspecao' in request.POST:
            return self.cancelar_inspecao(request)
        
        return redirect('em_aberto')

    def concluir_deteccao(self, request):
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        inspecao.deteccao_finalizada = True
        inspecao.deteccao_finalizada_at = now()
        inspecao.save()
        return redirect('colecao', pk=inspecao_id)
    
    def cancelar_inspecao(self, request):
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        inspecao.inspecao_finalizada = True
        inspecao.inspecao_cancelada = True
        inspecao.inspecao_finalizada_at = now()
        inspecao.save()
        return redirect('concluidas')
    

class colecao(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    model = Discrepancia
    template_name = 'colecao.html'
    context_object_name = 'discrepancias'

    def dispatch(self, request, *args, **kwargs):
        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])

        if inspecao.inspecao_finalizada:
            messages.error(request, "Acesso negado. A inspeção já foi finalizada.")
            return redirect(request.META.get('HTTP_REFERER', 'concluidas'))
        
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        inspecao_pk = Inspecao.objects.get(pk=self.kwargs['pk'])

        principais = Discrepancia_filtrada.objects.values_list('principal_id', flat=True)
        repetidas = Discrepancia_filtrada.objects.values_list('repetidas', flat=True)
        
        lista_nao_filtradas = Discrepancia.objects.filter(fonte=inspecao_pk).exclude(id__in=set(principais) | set(repetidas))

        return lista_nao_filtradas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['inspecao'] = self.kwargs['pk']

        inspecao = Inspecao.objects.filter(pk=self.kwargs['pk']).values('artefato', 'titulo').first()

        context['nomenclatura_especifica'] = Artefato.objects.filter(pk = inspecao['artefato']
            ).values('nomeclatura_espcifica').first()['nomeclatura_espcifica']
        
        context['nomenclatura_geral'] = Artefato.objects.filter(pk = inspecao['artefato']
            ).values('nomeclatura_geral').first()['nomeclatura_geral']
        
        context['titulo_inspecao'] = inspecao['titulo']

        return context
    
    def post(self, request, *args, **kwargs):
        if 'cancelar_inspecao' in request.POST:
            return self.cancelar_inspecao(request)
        
        return redirect('concluidas')
    
    def cancelar_inspecao(self, request):
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        if not inspecao.inspecao_finalizada:
            inspecao.inspecao_finalizada = True
        inspecao.inspecao_cancelada = True
        inspecao.inspecao_finalizada_at = now()
        inspecao.save()
        return redirect('concluidas')


class colecao_agrupar(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users-login')
    success_url = reverse_lazy('colecao')
    model = Discrepancia_filtrada
    template_name = 'colecao_agrupar.html'
    fields = ['repetidas']

    def dispatch(self, request, *args, **kwargs):
        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])

        if inspecao.inspecao_finalizada:
            messages.error(request, "Acesso negado. A inspeção já foi finalizada.")
            return redirect(request.META.get('HTTP_REFERER', 'concluidas'))
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            context['titulo_inspecao'] = Inspecao.objects.filter(pk=self.kwargs['pk']).first().titulo

            return context

    def get_success_url(self):
        return reverse_lazy('colecao', kwargs={'insp': self.kwargs.get('insp')})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        id_discrepancia_principal = self.kwargs.get('disc')
        id_inspecao_fonte = self.kwargs['pk']

        ja_filtradas = Discrepancia_filtrada.objects.filter(principal__fonte=self.kwargs.get('pk')).values_list("repetidas", "principal")
        lista_excluir = [item for tupla in ja_filtradas for item in tupla] + [id_discrepancia_principal]

        # Filtrar para que a discrepância principal e as já agrupadas não apareçam na lista de repetidas
        form.fields['repetidas'].queryset = Discrepancia.objects.filter(fonte=id_inspecao_fonte
            ).exclude(id__in=lista_excluir)

        return form

    def form_valid(self, form):
        id = get_object_or_404(Inspecao, pk=self.kwargs.get('pk')).pk
        discrepancia_principal = get_object_or_404(Discrepancia, pk=self.kwargs.get('disc'))
        print(discrepancia_principal)
        repetidas = form.cleaned_data.get('repetidas')

        
        discrepancia_filtrada = Discrepancia_filtrada.objects.create(principal=discrepancia_principal)
        
        if repetidas:
            discrepancia_filtrada.repetidas.set(repetidas)

        
        return redirect('colecao',pk = id)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    

    def post(self, request, *args, **kwargs):
        if 'concluir_colecao' in request.POST:
            return self.concluir_colecao(request)
        
        form = self.get_form()
    
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def concluir_colecao(self, request):
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        inspecao.colecao_finalizada = True
        inspecao.inspecao_finalizada_at = now()
        inspecao.save()
        return redirect('discriminacao', pk=inspecao_id)

    fields = ['repetidas']
    success_url = reverse_lazy('colecao')


class discriminacao(LoginRequiredMixin, View):
    login_url = reverse_lazy('users-login')
    template_name = 'discriminacao.html'

    def dispatch(self, request, *args, **kwargs):
        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])

        if inspecao.inspecao_finalizada:
            messages.error(request, "Acesso negado. A inspeção já foi finalizada.")
            return redirect(request.META.get('HTTP_REFERER', 'concluidas'))
        
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_formsets(request)

    def post(self, request, *args, **kwargs):
        if 'concluir_inspecao' in request.POST:
            return self.concluir_inspecao(request)
        elif 'cancelar_inspecao' in request.POST:
            return self.cancelar_inspecao(request)
        elif 'salvar_alteracoes' in request.POST:
            messages.info(request, "Status da inspeção salvo com sucesso!")
            return self.salvar_alteracoes(request)
        else:
            return self.render_formsets(request)


    def salvar_alteracoes(self, request):
        id_inspecao = self.kwargs['pk']
        discrepancias = Discrepancia_filtrada.objects.filter(principal__fonte= id_inspecao)
        id_artefato = Inspecao.objects.get(pk=self.kwargs['pk']).artefato.id
        all_forms_valid = True

        for discrepancia in discrepancias:
            form = DiscrepanciaFiltradaInlineForm(
                request.POST, 
                instance = discrepancia,
                artefato_id = id_artefato,
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
        self.salvar_alteracoes(request)
        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])
        inspecao.inspecao_finalizada = True
        inspecao.inspecao_finalizada_at = now()
        inspecao.save()
        return redirect('concluidas')
    
    def cancelar_inspecao(self, request):
        inspecao_id = self.kwargs['pk']
        inspecao = get_object_or_404(Inspecao, id=inspecao_id)
        if not inspecao.inspecao_finalizada:
            inspecao.inspecao_finalizada = True
        inspecao.inspecao_cancelada = True
        inspecao.inspecao_finalizada_at = now()
        inspecao.save()
        return redirect('concluidas')

    def render_formsets(self, request, post_data=None):
        id_inspecao = self.kwargs['pk']
        discrepancias = Discrepancia_filtrada.objects.filter(principal__fonte= id_inspecao)
        id_artefato = Inspecao.objects.get(pk=self.kwargs['pk']).artefato.id
        formsets = []

        for discrepancia in discrepancias:
            form = DiscrepanciaFiltradaInlineForm(
                post_data, 
                instance = discrepancia, 
                artefato_id = id_artefato,
                prefix=f'discrepancia_{discrepancia.id}'
            )
            formsets.append([discrepancia, form])

        inspecao = Inspecao.objects.get(pk=self.kwargs['pk'])
        titulo_inspecao = inspecao.titulo

        return render(request, self.template_name, {'formsets': formsets, 'titulo_inspecao': titulo_inspecao})

# Isso nem deveria estar aqui, muda para o arquivo: inspecao/views.py
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
        fontSize=11,
        leading=12
    )

    elements = [Paragraph(f'Título: {inspec.titulo}', style_header)]
    
    elements.append(Spacer(1, 20))

    discrepancias = Discrepancia_filtrada.objects.filter(principal__fonte=inspec)

    if(not discrepancias):
        messages.error(request, "Não há nenhuma discrepância filtrada associada a esta inspeção."+
                                " Esta inspeção nunca chegou à etapa de discriminação.")
        return redirect('concluidas')
    
    data = [['Localização', 'Descrição', 'Autor', 'Tipo', 'Severidade']]

    nomenclatura_geral = discrepancias[0].principal.fonte.artefato.nomeclatura_geral
    nomenclatura_especifica = discrepancias[0].principal.fonte.artefato.nomeclatura_espcifica

    for discrepancia in discrepancias:
        localizacao = nomenclatura_geral +' '+ discrepancia.principal.localizacao_geral +', '+ nomenclatura_especifica +' '+ discrepancia.principal.localizacao_especifica
        descricao = discrepancia.principal.descricao
        autor = discrepancia.principal.responsavel
        tipo = discrepancia.principal.tipo
        severidade = discrepancia.severidade
        data.append([
            Paragraph(localizacao, style_cels),
            Paragraph(descricao, style_cels),
            Paragraph(str(autor), style_cels),
            Paragraph(tipo, style_cels),
            Paragraph(str(severidade), style_cels)
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

    name = str(discrepancia.principal.fonte) + " - " + str(discrepancia.principal.fonte.artefato) + ".pdf"

    return FileResponse(buf, as_attachment=True, filename=name)