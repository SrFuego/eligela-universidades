# Python imports


# Django imports
from django.db import models


# Third party apps imports


# Local imports
from .choices import TIPO_CHOICES


# Create your models here.
class AreaAcademica(models.Model):
    """(Area Académica description)"""
    nombre = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    """(Carrera description)"""
    area_academica = models.ForeignKey(AreaAcademica)
    campo_laboral = models.TextField(blank=True)
    concepto = models.TextField(blank=True)
    costo_anual = models.PositiveSmallIntegerField(blank=True, null=True)
    habilidades = models.TextField(blank=True)
    mencion = models.CharField(blank=True, max_length=100)
    nombre = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    """(Departamento description)"""
    nombre = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre


class Institucion(models.Model):
    """(Instituciones description)"""
    acreditaciones = models.ManyToManyField(Carrera)
    nombre = models.CharField(blank=True, max_length=100)
    tipo = models.CharField(blank=True, max_length=100, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre
