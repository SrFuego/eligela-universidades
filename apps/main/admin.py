# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from import_export.admin import ImportExportModelAdmin


# Local imports
from .models import (
    AreaAcademica,
    Carrera,
    Departamento,
    Institucion,
)

from .resources import (
    AreaAcademicaResource,
    CarreraResource,
    DepartamentoResource,
    InstitucionResource,
)


# Register your models here.
@admin.register(AreaAcademica)
class AreaAcademicaAdmin(ImportExportModelAdmin):
    resource_class = AreaAcademicaResource

    ordering = ('-nombre',)


@admin.register(Carrera)
class CarreraAdmin(ImportExportModelAdmin):
    resource_class = CarreraResource

    list_display = (
        'nombre',
        'area_academica',
        'campo_laboral',
        'concepto',
        'costo_anual',
        'habilidades',
        'mencion',
        )
    list_filter = (
        'nombre',
        'area_academica',
        'costo_anual',
        )
    ordering = ('-nombre', '-area_academica', '-costo_anual')


@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin):
    resource_class = DepartamentoResource

    ordering = ('-nombre',)


@admin.register(Institucion)
class InstitucionAdmin(ImportExportModelAdmin):
    resource_class = InstitucionResource

    list_display = (
        'nombre',
        'tipo',
    )
    list_filter = ('tipo', 'acreditaciones',)
    ordering = ('-nombre', '-tipo',)
