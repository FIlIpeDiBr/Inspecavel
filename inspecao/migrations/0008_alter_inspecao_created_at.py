# Generated by Django 5.0.6 on 2025-01-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecao', '0007_alter_inspecao_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspecao',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
