# Generated by Django 4.0.6 on 2023-02-23 02:
from django.db import migrations
import os


def carga():
    from django.conf import settings
    BASE_DIR = settings.BASE_DIR
    consulta = open(os.path.join(BASE_DIR,'sql/migraciones.sql'),'r').read()
    return consulta

class Migration(migrations.Migration):

    dependencies = [
        ('clientes_orm', '0002_area_estudio_personal'),
    ]

    operations = [
        migrations.RunSQL(carga(),)
    ]
