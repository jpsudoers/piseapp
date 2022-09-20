from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Establecimiento)
admin.site.register(models.Matricula)

admin.site.register(models.Mail)
admin.site.register(models.CorreosEstablecimiento)
admin.site.register(models.Alerta)

admin.site.register(models.CasoVulneracion)

admin.site.register(models.Discriminacion)
admin.site.register(models.MedidasDiscriminacion)

admin.site.register(models.Maltrato)
admin.site.register(models.MedidasMaltrato)

admin.site.register(models.ConnotacionSexual)

admin.site.register(models.AccidenteEscolar)

admin.site.register(models.FuncionarioEstablecimiento)

admin.site.register(models.VulneracionDerechosFuncionarios)

#class MatriculaEstablecimientoResourceAdmin(ImportExportModelAdmin):
#    resource_class = MatriculaEstablecimientoResource
#admin.site.register(models.Matricula,MatriculaEstablecimientoResourceAdmin)
