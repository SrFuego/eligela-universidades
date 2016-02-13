# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('campo_laboral', models.TextField(blank=True)),
                ('concepto', models.TextField(blank=True)),
                ('costo_anual', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('habilidades', models.TextField(blank=True)),
                ('mencion', models.CharField(max_length=100, blank=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('area_academica', models.ForeignKey(to='main.AreaAcademica')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('tipo', models.CharField(max_length=100, blank=True, choices=[('0', 'Estatal'), ('1', 'Particular')])),
                ('acreditaciones', models.ManyToManyField(to='main.Carrera')),
            ],
        ),
    ]
