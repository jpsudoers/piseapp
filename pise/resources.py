from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from pise.models import Alumno, Establecimiento, Matricula

class MatriculaEstablecimientoResource(resources.ModelResource):
    alumno = fields.Field(column_name='alumno', attribute='alumno', widget=ForeignKeyWidget(Alumno, field='alumno'))
    establecimiento = fields.Field(column_name='establecimiento', attribute='establecimiento', widget=ForeignKeyWidget(Establecimiento, field='name'))
    class Meta:
        model = Matricula
        fields =('alumno','establecimiento','nivel','letra','fecha_incorporacion','fecha_retiro')