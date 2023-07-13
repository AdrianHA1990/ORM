# Generated by Django 4.0.6 on 2023-03-04 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificacion', models.DateField(auto_now_add=True, verbose_name='Fecha Modificacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificacion', models.DateField(auto_now_add=True, verbose_name='Fecha Modificacion')),
                ('name_categorias', models.CharField(max_length=50, verbose_name='Categorias')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FichaAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificacion', models.DateField(auto_now_add=True, verbose_name='Fecha Modificacion')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('year', models.CharField(max_length=50, verbose_name='Año')),
                ('costo', models.FloatField(default=0, verbose_name='Costo')),
                ('dias_renta', models.PositiveBigIntegerField(default=0, verbose_name='Dias')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificacion', models.DateField(auto_now_add=True, verbose_name='Fecha Modificacion')),
                ('nombre_interes', models.CharField(max_length=50, verbose_name='Interes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificacion', models.DateField(auto_now_add=True, verbose_name='Fecha Modificacion')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('interes', models.ManyToManyField(to='personas_orm.interes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificacion', models.DateField(auto_now_add=True, verbose_name='Fecha Modificacion')),
                ('fecha_dev', models.DateTimeField(blank=True, null=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas_orm.auto')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas_orm.personas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatosP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificacion', models.DateField(auto_now_add=True, verbose_name='Fecha Modificacion')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
                ('nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
                ('direction', models.CharField(max_length=50, verbose_name='Direccion')),
                ('tel', models.CharField(max_length=50, verbose_name='Telefono')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas_orm.personas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='auto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas_orm.categorias'),
        ),
        migrations.AddField(
            model_name='auto',
            name='ficha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas_orm.fichaauto'),
        ),
    ]