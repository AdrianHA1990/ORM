# Generated by Django 4.0.6 on 2023-02-24 00:30
from django.db import migrations
import os


def carga_nueva():
    from django.conf import settings
    BASE_DIR = settings.BASE_DIR
    consulta = open(os.path.join(BASE_DIR, 'sql/migraciones2.sql'), 'r', encoding="UTF8").read()
    return consulta

class Migration(migrations.Migration):

    dependencies = [
        ('clientes_orm', '0003_auto_20230222_2040'),
    ]

    operations = [
        migrations.RunSQL(carga_nueva(),)
    ]
