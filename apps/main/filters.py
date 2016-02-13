# Python imports


# Django imports


# Third party apps imports
import django_filters


# Local imports
from .models import (
    AreaAcademica,
    Carrera,
    Departamento,
    Institucion,
)


# Create your filters here.
class AreaAcademicaFilter(django_filters.FilterSet):
    class Meta:
        model = AreaAcademica
        fields = (
            'nombre',
        )


class CarreraFilter(django_filters.FilterSet):
    class Meta:
        model = Carrera
        fields = (
            'area_academica',
            'costo_anual',
            'nombre',
        )


class DepartamentoFilter(django_filters.FilterSet):
    class Meta:
        model = Departamento
        fields = (
            'nombre',
        )


class InstitucionFilter(django_filters.FilterSet):
    class Meta:
        model = Institucion
        fields = (
            'nombre',
            'tipo',
        )
