# Python imports


# Django imports
from django.views.generic.base import TemplateView


# Third party apps imports


# Local imports
from .models import (
    AreaAcademica,
    Carrera,
    Departamento,
    Institucion,
    )

from .filters import (
    AreaAcademicaFilter,
    CarreraFilter,
    DepartamentoFilter,
    InstitucionFilter,
    )


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'filter': CarreraFilter(self.request.GET,
                                    queryset=Carrera.objects.all()
                                    )
            }
        return context
