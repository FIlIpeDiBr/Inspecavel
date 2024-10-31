from django.db import migrations
from django.conf import settings

def inserir_admin(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

def remover_admin(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    User.objects.filter(username='admin').delete()

def inserir_usuarios_exemplo(apps, schema_editor):
        User = apps.get_model(settings.AUTH_USER_MODEL)
        
        User.objects.create_user(
            username = 'usuario01',
            email = 'usuario01@example.com',
            password = 'usuario01',
            first_name = 'usuario',
            last_name = 'Zeroum'
        )
        
        User.objects.create_user(
            username = 'usuario02',
            email = 'usuario02@example.com',
            password = 'usuario02',
            first_name = 'usuario',
            last_name = 'Zerdois'
        )
        
        User.objects.create_user(
            username = 'usuario03',
            email = 'usuario03@example.com',
            password = 'usuario03',
            first_name = 'usuario',
            last_name = 'Zerotres'
        )
        
        User.objects.create_user(
            username = 'usuario04',
            email = 'usuario04@example.com',
            password = 'usuario04',
            first_name = 'usuario',
            last_name = 'Zeroquatro'
        )

def deletar_usuarios_exemplo(apps, schema_editor):
        User = apps.get_model(settings.AUTH_USER_MODEL)  
        
        User.objects.filter(username__in=["Usuario01", "Usuario02", "Usuario03", "Usuario04"]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(inserir_admin, remover_admin),
        migrations.RunPython(inserir_usuarios_exemplo, deletar_usuarios_exemplo),
    ]