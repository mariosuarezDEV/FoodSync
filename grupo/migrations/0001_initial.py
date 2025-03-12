# Generated by Django 5.1.7 on 2025-03-12 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del grupo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado del grupo')),
                ('categoria', models.ManyToManyField(to='categoria.modelcategoria', verbose_name='Categoria ')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'db_table': 'grupo',
            },
        ),
        migrations.CreateModel(
            name='ModelSubGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del subgrupo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado del subgrupo')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupo.modelgrupo', verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'SubGrupo',
                'verbose_name_plural': 'SubGrupos',
                'db_table': 'subgrupo',
            },
        ),
    ]
