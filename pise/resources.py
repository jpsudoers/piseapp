from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from pise import models
from pise.models import Matricula

class MatriculaResource(resources.ModelResource):
    class Meta:
        model = models.Matricula
        exclude = ('nombre_apoderado','establecimiento','esta_activo')
        #fields = ('rut','dv','nombres','apellido_paterno','apellido_materno','domicilio_actual','Comuna_residencia','email','telefono','celular','fecha_nacimiento','codigo_etnia','nivel','letra','año','fecha_incorporacion','fecha_retiro')
