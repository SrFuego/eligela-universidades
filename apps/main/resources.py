# Python imports


# Django imports


# Third party apps imports
from import_export.resources import ModelResource


# Local imports
from .models import (
    AreaAcademica,
    Carrera,
    Departamento,
    Institucion,
)


# Create your resources here.


class AreaAcademicaResource(ModelResource):

    class Meta:
        model = AreaAcademica
        fields = (
            'id',
            'nombre',
            )


class CarreraResource(ModelResource):

    class Meta:
        model = Carrera
        fields = (
            'id',
            'area_academica',
            'campo_laboral',
            'concepto',
            'costo_anual',
            'habilidades',
            'mencion',
            'nombre',
            )


class DepartamentoResource(ModelResource):

    class Meta:
        model = Departamento
        fields = (
            'id'
            'nombre',
            )


class InstitucionResource(ModelResource):

    class Meta:
        model = Institucion
        fields = (
            'id',
            'acreditaciones',
            'nombre',
            'tipo',
            )
