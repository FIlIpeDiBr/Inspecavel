from django.db import migrations
from django.conf import settings

def inserir_artefato_base(apps, schema_editor):
    Artefato = apps.get_model('artefato', 'Artefato')
    Artefato.objects.create(
        titulo = "Inspeção de Usabilidade",
        nomeclatura_geral = "Tela",
        formato_geral = True,
        nomeclatura_espcifica = "Elemento",
        formato_especifico = True,
        tipo_defeito = "Omissão; Fato incorreto; Ambiguidade; Informação Estranha; Informação inconsistente",
        lista_severidade = "Não Defeito; Cosmético; Leve; Moderado; Grave; Catastrófico"
    )
def remover_artefeto_base(apps, schema_editor):
    Artefato = apps.get_model('artefato', 'Artefato')
    Artefato.objects.filter(titulo="Inspeção de Usabilidade")



class Migration(migrations.Migration):
    dependencies = [
        ('artefato', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(inserir_artefato_base, remover_artefeto_base),
    ]