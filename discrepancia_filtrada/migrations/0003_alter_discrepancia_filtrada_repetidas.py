# Generated by Django 5.0.6 on 2024-10-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discrepancia', '0003_initial'),
        ('discrepancia_filtrada', '0002_alter_discrepancia_filtrada_repetidas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discrepancia_filtrada',
            name='repetidas',
            field=models.ManyToManyField(blank=True, related_name='discrepancias_repetidas', to='discrepancia.discrepancia'),
        ),
    ]
