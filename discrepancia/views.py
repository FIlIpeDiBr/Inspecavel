import io
from django.http import FileResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from discrepancia.forms import DiscrepanciaForm
from discrepancia.models import Discrepancia

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, TableStyle, LongTable, SimpleDocTemplate, Spacer


class deteccao_inspetor(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users-login')
    template_name = 'deteccao_inspetor.html'
    success_url = reverse_lazy('users-login')
    form_class = DiscrepanciaForm
    model = Discrepancia

    def form_valid(self, form):
        form.instance.inspetor = self.request.user
        return super().form_valid(form)

class deteccao_monitor(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'deteccao_monitor.html'

class colecao(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'colecao.html'

class colecao_agrupar(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'colecao_agrupar.html'

class discriminacao(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users-login')
    template_name = 'discriminacao.html'


@login_required
def exportar_dados(request):
    discrepancias = Discrepancia.objects.all()
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

    for discrepancia in discrepancias:
        data = [[Paragraph(discrepancia.descricao, style_header)], ['Código', 'Atividade', 'CH Realizada', 'AP Máximo']]
        # aproveitamentos = Aproveitamento.objects.filter(aluno=aluno)
        # codigos = aproveitamentos.values('categoria__codigo').annotate(total_ch=Sum('ch'))

        # for codigo in codigos:
        #     aproveitamento_maximo = (
        #         Aproveitamento.objects.filter(categoria__codigo=codigo['categoria__codigo']).first().categoria.ap_max)
        #     descricao = (
        #         Aproveitamento.objects.filter(
        #             categoria__codigo=codigo['categoria__codigo']).first().categoria.descricao)
        #     data.append([codigo["categoria__codigo"],
        #                  Paragraph(descricao, style_cels),
        #                  codigo["total_ch"],
        #                  aproveitamento_maximo])
        table = LongTable(data, colWidths=[50, '*', 80, 80])
        elements.append(table)
        # elements.append(Spacer(1, 20))

        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('SPAN', (0, 0), (3, 0)),
            ('TOPPADDING', (0, 0), (-1, -1), 10),  # Adiciona espaço no topo das células
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))

    doc.build(elements)
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='relatorio.pdf')