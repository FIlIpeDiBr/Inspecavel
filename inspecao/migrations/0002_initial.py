# Generated by Django 5.0.7 on 2024-08-05 05:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inspecao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='inspecao',
            name='inspetores',
            field=models.ManyToManyField(related_name='inspetores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inspecao',
            name='moderador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
