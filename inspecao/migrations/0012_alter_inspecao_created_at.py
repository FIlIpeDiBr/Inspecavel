# Generated by Django 5.0.6 on 2025-01-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecao', '0011_alter_inspecao_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspecao',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
