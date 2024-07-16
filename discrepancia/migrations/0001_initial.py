# Generated by Django 5.0.7 on 2024-07-16 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inspecao', '0002_alter_inspecao_options'),
        ('inspetor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discrepancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
                ('localizacao', models.CharField(max_length=50, verbose_name='Localização')),
                ('tipo', models.CharField(max_length=30)),
                ('fonte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inspecao.inspecao')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inspetor.inspetor', verbose_name='Responsável')),
            ],
            options={
                'verbose_name': 'Discrepância',
                'verbose_name_plural': 'Discrepâncias',
            },
        ),
    ]
