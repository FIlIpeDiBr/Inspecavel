# Generated by Django 5.0.7 on 2024-08-05 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artefato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('nomeclatura_geral', models.CharField(max_length=30, verbose_name='Nomeclatura geral')),
                ('formato_geral', models.BooleanField(verbose_name='Formato geral permite letras?')),
                ('nomeclatura_espcifica', models.CharField(max_length=20, verbose_name='Nomeclatura específica')),
                ('formato_especifico', models.BooleanField(verbose_name='Formato específico permite letras?')),
                ('tipo_defeito', models.CharField(max_length=100)),
                ('lista_severidade', models.CharField(max_length=100)),
            ],
        ),
    ]
